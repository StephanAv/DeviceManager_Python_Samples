#ifndef PY_MAINBOARD_H
#define PY_MAINBOARD_H

#include <Python.h>
#include "py_slot_templates.h"
#include "mainboard.h"

typedef DObject<DeviceManager::Mainboard> MbType;

namespace Mainboard {
    PyObject* serialNumber(PyObject* self, PyObject* args);
    PyObject* getMinTemp(PyObject* self, PyObject* args);
    PyObject* getMaxTemp(PyObject* self, PyObject* args);
    PyObject* getTemp(PyObject* self, PyObject* args);
}

static PyMethodDef MbType_methods[] = {
    {"serialNumber", (PyCFunction)Mainboard::serialNumber, METH_NOARGS, "Get the serial number of the mainboard"},
    {"getMinTemp", (PyCFunction)Mainboard::getMinTemp, METH_NOARGS, "Get the minimal mainboard temperature"},
    {"getMaxTemp", (PyCFunction)Mainboard::getMaxTemp, METH_NOARGS, "Get the maximal mainboard temperature"},
    {"getTemp", (PyCFunction)Mainboard::getTemp, METH_NOARGS, "Get the current mainboard temperature"},
    {NULL, NULL} /* Sentinel */
};

static PyType_Slot MbType_slots[] = {
    {Py_tp_new, (void*)dtype_new<DeviceManager::Mainboard>},
    {Py_tp_init, (void*)dtype_init<DeviceManager::Mainboard>},
    {Py_tp_dealloc, (void*)dtype_dealloc<DeviceManager::Mainboard>},
    {Py_tp_methods, MbType_methods},
    {0, 0} /* Sentinel */
};

static PyType_Spec MbType_spec = {
    "Mainboard", // tp_name
    #if defined(USE_TWINCAT_ROUTER)
    sizeof(MbType) + sizeof(TC1000AdsClient), // tp_basicsize
#else
    sizeof(MbType) + sizeof(GenericAdsClient),
#endif
    0, // tp_itemsize : All instances have the same size
    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,
    MbType_slots
};

#endif