#include <Python.h>
#include "twincat.h"
#include "py_twincat.h"
#include "ads_py_error.h"

PyObject* getTcMajor(PyObject* self, PyObject* Py_UNUSED(args))
{
    TcType* self_tc = reinterpret_cast<TcType*>(self);

    uint16_t major = 0;
    int32_t ret = self_tc->m_dtype->getTcMajor(major);

    if (ret) {
        PyErr_SetObject(PyExc_RuntimeError, adsErrorStr(ret));
        return NULL;
    }

    return PyLong_FromUnsignedLong(major);
}

PyObject* getTcMinor(PyObject* self, PyObject* Py_UNUSED(args))
{
    TcType* self_tc = reinterpret_cast<TcType*>(self);

    uint16_t minor = 0;
    int32_t ret = self_tc->m_dtype->getTcMinor(minor);

    if (ret) {
        PyErr_SetObject(PyExc_RuntimeError, adsErrorStr(ret));
        return NULL;
    }

    return PyLong_FromUnsignedLong(minor);
}

PyObject* getTcBuild(PyObject* self, PyObject* Py_UNUSED(args))
{
    TcType* self_tc = reinterpret_cast<TcType*>(self);

    uint16_t build = 0;
    int32_t ret = self_tc->m_dtype->getTcBuild(build);

    if (ret) {
        PyErr_SetObject(PyExc_RuntimeError, adsErrorStr(ret));
        return NULL;
    }

    return PyLong_FromUnsignedLong(build);
}

PyObject* deleteAdsRoute(PyObject* self, PyObject* args)
{
    TcType* self_tc = reinterpret_cast<TcType*>(self);

    char* route = NULL;
    if (!PyArg_ParseTuple(args, "s", &route)) {
        return NULL;
    }

    int32_t ret = self_tc->m_dtype->deleteAdsRoute(route);
    if (ret) {
        PyErr_SetObject(PyExc_RuntimeError, adsErrorStr(ret));
        return NULL;
    }
    Py_RETURN_NONE;
}