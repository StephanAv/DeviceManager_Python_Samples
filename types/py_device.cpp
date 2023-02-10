#include <Python.h>
#include "BDM_DeviceArea.h"
#include "py_device.h"
#include "ads_py_error.h"

PyObject* serialNumber(PyObject* self, PyObject* args)
{
	DeviceType* self_device = reinterpret_cast<DeviceType*>(self);
	std::string serialNumber;

	int32_t ret = self_device->m_dtype->getSerialNumber(serialNumber);
	if (ret) {
		PyErr_SetObject(PyExc_RuntimeError, adsErrorStr(ret));
		return NULL;
	}

	return PyUnicode_FromString(serialNumber.c_str());
}