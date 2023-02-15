#ifndef PY_SLOT_TEMPLATES_H
#define PY_SLOT_TEMPLATES_H

#include <Python.h>
#include <cstddef>
#include <iostream>
#include <cstdint>
#include <sstream>
#include <stdexcept>
#include <string>

#if defined(USE_TWINCAT_ROUTER)
	#include "TC1000_AdsClient.h"
#else
	#include "GenericAdsClient.h"
#endif

#include "ads_exception.h"

template <typename T>
struct DObject{
    PyObject_HEAD
    BasicADS* m_ads;
    T *m_dtype;
};

template <typename T>
PyObject *dtype_new(PyTypeObject *type){
    // std::cout << typeid(T).name() <<"_new() called" << std::endl;
    DObject<T> *self;

        self = (DObject<T>*) type->tp_alloc(type, 0);
        if (self != NULL) {
            self->m_ads = NULL;
            self->m_dtype = NULL;
        } else {
            return PyErr_NoMemory();
        }
       return (PyObject*) self;
}

template <typename T>
int dtype_init(PyObject *self, PyObject *args, PyObject *kwds){
    // std::cout << typeid(T).name() <<"_init() called" << std::endl;
    assert(args);

    // Process Python arguments
    char *amsAddr = NULL;
#if defined(USE_TWINCAT_ROUTER)
    if (!PyArg_ParseTuple(args, "s", &amsAddr)) {
        return -1;
    }
#else
    char *ipAddr  = NULL;
    // TODO oder ss
    if (!PyArg_ParseTuple(args, "ss", &amsAddr, &ipAddr)) {
        return -1;
    }
#endif

    // Parse AmsNetId

    uint8_t b_netId[6]  = { 0, 0, 0, 0, 1, 1 };
    size_t i = 0;
    std::istringstream s_amsAddr(amsAddr);
    std::string token;

    while((i < sizeof(b_netId)) && std::getline(s_amsAddr, token, '.')){
        try {
            b_netId[i++] = std::stoi(token);
        } catch (std::logic_error const& ex) {
            std::string err("Error parsing AmsNetId: ");
            err += ex.what(); 
            PyErr_SetString(PyExc_RuntimeError, err.c_str());
            return -1;
        }
    }

    static const AmsNetId remoteNetId{ b_netId[0], b_netId[1], b_netId[2], b_netId[3], b_netId[4], b_netId[5] };

    DObject<T> *self_dtype = reinterpret_cast<DObject<T>*>(self);

    // Allocation and instatiation of the ADS client
#if defined(USE_TWINCAT_ROUTER)
    
    self_dtype->m_ads = (BasicADS*)PyObject_Malloc(sizeof(TC1000AdsClient));
    if (!self_dtype->m_ads) {
        PyErr_SetNone(PyExc_MemoryError);
        return -1;
    }

    try {
        new (self_dtype->m_ads) TC1000AdsClient(remoteNetId);
    }
    catch (const std::exception& ex) {
        std::cout << "ADS Exception" << std::endl;
        PyObject_Free(self_dtype->m_ads);
        self_dtype->m_ads = NULL;
        PyErr_SetString(PyExc_RuntimeError, ex.what());
        return -1;
    }

#else

    self_dtype->m_ads = (BasicADS*)PyObject_Malloc(sizeof(GenericAdsClient));
    if(!self_dtype->m_ads){
        PyErr_SetNone(PyExc_MemoryError);
        return -1;
    }

    try{
        new (self_dtype->m_ads) GenericAdsClient(remoteNetId, ipAddr);
    } catch (const AdsException &ex) {
        std::cout << "ADS Exception" << std::endl;
        PyObject_Free(self_dtype->m_ads);
        self_dtype->m_ads = NULL;
        PyErr_SetString(PyExc_RuntimeError, ex.what());
        return -1;
    } catch (const std::runtime_error &ex) {
        std::cout << "Runtime error" << std::endl;
        PyObject_Free(self_dtype->m_ads);
        self_dtype->m_ads = NULL;
        PyErr_SetString(PyExc_RuntimeError, ex.what());
        return -1;
    }
#endif

    // Memory allocation for Device Manager type
    self_dtype->m_dtype = (T*)PyObject_Malloc(sizeof(T));
    if(!self_dtype->m_dtype){
        PyErr_SetNone(PyExc_MemoryError);
        return -1;
    }

	try {
        new (self_dtype->m_dtype) T(*self_dtype->m_ads);
	}
	catch (const DeviceManager::AdsException& ex) {
        PyErr_SetString(PyExc_RuntimeError, ex.what());
		return -1;
	}

	if (!self_dtype->m_dtype) {
        PyErr_SetString(PyExc_RuntimeError, "Module not available on target");
		return -1;
	}

    return 0;
}

template<typename T>
void dtype_dealloc(PyObject *self){
    //std::cout << typeid(T).name() <<"_dealloc() called" << std::endl;
    DObject<T> *self_dtype = reinterpret_cast<DObject<T>*>(self);

    if(self_dtype->m_dtype){
        self_dtype->m_dtype->~T();
        PyObject_Free(self_dtype->m_dtype);
    }

    if(self_dtype->m_ads){
        self_dtype->m_ads->~BasicADS();
        PyObject_Free(self_dtype->m_ads);
    }
}
#endif