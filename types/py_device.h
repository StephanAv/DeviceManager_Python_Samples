#ifndef PY_DEVICE_H
#define PY_DEVICE_H

#include <Python.h>
#include "py_slot_templates.h"
#include "BDM_DeviceArea.h"

typedef DObject<DeviceManager::DeviceArea> DeviceType;

PyObject* serialNumber(PyObject* self, PyObject* args);

static PyMethodDef DeviceType_methods[] = {
    {"serialNumber", (PyCFunction)serialNumber, METH_NOARGS, "Get the serial number of the target system"},
    {NULL, NULL} /* Sentinel */
};

static PyType_Slot DeviceType_slots[] = {
    {Py_tp_new, (void*)dtype_new<DeviceManager::DeviceArea>},
    {Py_tp_init, (void*)dtype_init<DeviceManager::DeviceArea>},
    {Py_tp_dealloc, (void*)dtype_dealloc<DeviceManager::DeviceArea>},
    {Py_tp_methods, DeviceType_methods},
    {0, 0} /* Sentinel */
};

static PyType_Spec DeviceType_spec = {
    "Device", // tp_name
    #if defined(USE_TWINCAT_ROUTER)
    sizeof(DeviceType) + sizeof(TC1000AdsClient), // tp_basicsize
#else
    sizeof(DeviceType) + sizeof(GenericAdsClient),
#endif
    0, // tp_itemsize : All instances have the same size
    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,
    DeviceType_slots
};

#endif