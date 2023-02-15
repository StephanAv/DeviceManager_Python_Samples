#ifndef PY_GENERAL_H
#define PY_GENERAL_H

#include <Python.h>
#include "py_slot_templates.h"
#include "BDM_GeneralArea.h"

typedef DObject<DeviceManager::GeneralArea> GenType;

PyObject* deviceName(PyObject* self, PyObject* args);


static PyMethodDef GenType_methods[] = {
    {"deviceName", (PyCFunction)deviceName, METH_VARARGS, "Get the name of the target device"},
    {NULL, NULL} /* Sentinel */
};

static PyType_Slot GenType_slots[] = {
    {Py_tp_new, (void*)dtype_new<DeviceManager::GeneralArea>},
    {Py_tp_init, (void*)dtype_init<DeviceManager::GeneralArea>},
    {Py_tp_dealloc, (void*)dtype_dealloc<DeviceManager::GeneralArea>},
    {Py_tp_methods, GenType_methods},
    {0, 0} /* Sentinel */
};

static PyType_Spec GenType_spec = {
    "General", // tp_name
    #if defined(USE_TWINCAT_ROUTER)
    sizeof(GenType) + sizeof(TC1000AdsClient), // tp_basicsize
#else
    sizeof(GenType) + sizeof(GenericAdsClient),
#endif
    0, // tp_itemsize : All instances have the same size
    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,
    GenType_slots
};

#endif