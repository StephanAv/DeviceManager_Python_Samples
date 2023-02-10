#ifndef PY_MISCELLANEOUS_H
#define PY_MISCELLANEOUS_H

#include <Python.h>
#include "py_slot_templates.h"
#include "miscellaneous.h"

typedef DObject<DeviceManager::Miscellaneous> MiscType;

PyObject* reboot(PyObject* self, PyObject* args);


static PyMethodDef MiscType_methods[] = {
    {"reboot", (PyCFunction)reboot, METH_NOARGS, "Reboot target system"},
    {NULL, NULL} /* Sentinel */
};

static PyType_Slot MiscType_slots[] = {
    {Py_tp_new, (void*)dtype_new<DeviceManager::Miscellaneous>},
    {Py_tp_init, (void*)dtype_init<DeviceManager::Miscellaneous>},
    {Py_tp_dealloc, (void*)dtype_dealloc<DeviceManager::Miscellaneous>},
    {Py_tp_methods, MiscType_methods},
    {0, 0} /* Sentinel */
};

static PyType_Spec MiscType_spec = {
    "Miscellaneous", // tp_name
    #if defined(USE_TWINCAT_ROUTER)
    sizeof(MiscType) + sizeof(TC1000AdsClient), // tp_basicsize
#else
    sizeof(MiscType) + sizeof(GenericAdsClient),
#endif
    0, // tp_itemsize : All instances have the same size
    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,
    MiscType_slots
};
#endif