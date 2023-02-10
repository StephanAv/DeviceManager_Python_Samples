#include <Python.h>
#include "py_cpu.h"
#include "py_twincat.h"
#include "py_fso.h"
#include "py_mainboard.h"
#include "py_miscellaneous.h"
#include "py_general.h"
#include "py_device.h"

PyModuleDef devman_module = {
    PyModuleDef_HEAD_INIT,
    "DeviceManager", // Module name
    "Allows to access various properties of Beckhoff IPCs",
    -1,   // Optional size of the module state memory
    NULL, // Optional method definitions
    NULL, // Optional slot definitions
    NULL, // Optional traversal function
    NULL, // Optional clear function
    NULL  // Optional module deallocation function
};

void decref(std::vector<PyObject*>& vDecr) {
    for (auto& pPyObj : vDecr){
        Py_DecRef(pPyObj);
    }
}

PyMODINIT_FUNC 
PyInit_DeviceManager(void) {

    std::vector<PyObject*> vDecr;
    PyObject* module = PyModule_Create(&devman_module);
    vDecr.push_back(module);

    // Create and add CPU type

    PyObject *cpu_type = PyType_FromSpec(&CpuType_spec);
    if (cpu_type == NULL){
        decref(vDecr);
        return NULL;
    }
    vDecr.push_back(cpu_type);

    if(PyModule_AddObject(module, "CPU", cpu_type) < 0){
        decref(vDecr);
        return NULL;
    }

    // Create and add TwinCAT type
    PyObject* tc_type = PyType_FromSpec(&TcType_spec);
    if (tc_type == NULL) {
        decref(vDecr);
        return NULL;
    }
    vDecr.push_back(tc_type);

    if (PyModule_AddObject(module, "TwinCAT", tc_type) < 0) {
        decref(vDecr);
        return NULL;
    }

    // Create and add File System Object type
    PyObject* fso_type = PyType_FromSpec(&FsoType_spec);
    if (fso_type == NULL) {
        decref(vDecr);
        return NULL;
    }
    vDecr.push_back(fso_type);

    if (PyModule_AddObject(module, "FileSystem", fso_type) < 0) {
        decref(vDecr);
        return NULL;
    }

    // Create and add mainboard type
    PyObject* mb_type = PyType_FromSpec(&MbType_spec);
    if (mb_type == NULL) {
        decref(vDecr);
        return NULL;
    }
    vDecr.push_back(mb_type);

    if (PyModule_AddObject(module, "Mainboard", mb_type) < 0) {
        decref(vDecr);
        return NULL;
    }

    // Create and add Miscellaneous type
    PyObject* misc_type = PyType_FromSpec(&MiscType_spec);
    if (misc_type == NULL) {
        decref(vDecr);
        return NULL;
    }
    vDecr.push_back(misc_type);

    if (PyModule_AddObject(module, "Miscellaneous", misc_type) < 0) {
        decref(vDecr);
        return NULL;
    }

    // Create and add general area type
    PyObject* gen_type = PyType_FromSpec(&GenType_spec);
    if (gen_type == NULL) {
        decref(vDecr);
        return NULL;
    }
    vDecr.push_back(gen_type);

    if (PyModule_AddObject(module, "General", gen_type) < 0) {
        decref(vDecr);
        return NULL;
    }

    // Create and add general device type
    PyObject* device_type = PyType_FromSpec(&DeviceType_spec);
    if (device_type == NULL) {
        decref(vDecr);
        return NULL;
    }
    vDecr.push_back(device_type);

    if (PyModule_AddObject(module, "Device", device_type) < 0) {
        decref(vDecr);
        return NULL;
    }

    return module;
}