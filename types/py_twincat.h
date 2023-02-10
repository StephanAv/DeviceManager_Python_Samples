#ifndef PY_TWINCAT_H
#define PY_TWINCAT_H

#include <Python.h>
#include "py_slot_templates.h"
#include "twincat.h"

typedef DObject<DeviceManager::TwinCAT> TcType;

PyObject* getTcMajor(PyObject* self, PyObject* args);
PyObject* getTcMinor(PyObject* self, PyObject* args);
PyObject* getTcBuild(PyObject* self, PyObject* args);
PyObject* deleteAdsRoute(PyObject* self, PyObject* args);

static PyMethodDef TcType_methods[] = {
    {"getTcMajor", (PyCFunction)getTcMajor, METH_NOARGS, "Return TwinCAT major version number"},
    {"getTcMinor", (PyCFunction)getTcMinor, METH_NOARGS, "Return TwinCAT minor version number"},
    {"getTcBuild", (PyCFunction)getTcBuild, METH_NOARGS, "Returns TwinCAT build number"},
    {"deleteAdsRoute", (PyCFunction)deleteAdsRoute, METH_VARARGS, "Deletes given ADS route"},
    {NULL, NULL} /* Sentinel */
};

static PyType_Slot TcType_slots[] = {
    {Py_tp_new, (void*)dtype_new<DeviceManager::TwinCAT>},
    {Py_tp_init, (void*)dtype_init<DeviceManager::TwinCAT>},
    {Py_tp_dealloc, (void*)dtype_dealloc<DeviceManager::TwinCAT>},
    {Py_tp_methods, TcType_methods},
    {0, 0} /* Sentinel */
};

static PyType_Spec TcType_spec = {
    "TwinCAT", // tp_name
    #if defined(USE_TWINCAT_ROUTER)
    sizeof(TcType) + sizeof(TC1000AdsClient), // tp_basicsize
#else
    sizeof(TcType) + sizeof(GenericAdsClient),
#endif
    0, // tp_itemsize : All instances have the same size
    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,
    TcType_slots
};
#endif