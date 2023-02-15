#include <Python.h>
#include "cpu.h"
#include "py_cpu.h"
#include "ads_py_error.h"

PyObject* getTemp(PyObject *self, PyObject *args)
{
    CpuType* self_cpu = reinterpret_cast<CpuType*>(self);

    int16_t temp = 0;
    int32_t ret = self_cpu->m_dtype->getTemp(temp);

    if(ret){
        PyErr_SetObject(PyExc_RuntimeError, adsErrorStr(ret));
        return NULL;
    }

    return PyLong_FromUnsignedLong(temp);
}

PyObject* getFreq(PyObject* self, PyObject* args)
{
    CpuType* self_cpu = reinterpret_cast<CpuType*>(self);

    uint32_t freq = 0;
    int32_t ret = self_cpu->m_dtype->getFrequency(freq);

    if (ret) {
        PyErr_SetObject(PyExc_RuntimeError, adsErrorStr(ret));
        return NULL;
    }

    return PyLong_FromUnsignedLong(freq);
}

PyObject* getUsage(PyObject* self, PyObject* args)
{
    CpuType* self_cpu = reinterpret_cast<CpuType*>(self);

    uint16_t usage = 0;
    int32_t ret = self_cpu->m_dtype->getUsage(usage);

    if (ret) {
        PyErr_SetObject(PyExc_RuntimeError, adsErrorStr(ret));
        return NULL;
    }

    return PyLong_FromUnsignedLong(usage);
}