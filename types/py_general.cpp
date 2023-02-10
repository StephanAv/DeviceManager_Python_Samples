#include <Python.h>
#include "BDM_GeneralArea.h"
#include "py_general.h"
#include "ads_py_error.h"

PyObject* deviceName(PyObject* self, PyObject* args)
{
	GenType* self_gen = reinterpret_cast<GenType*>(self);
	std::string deviceName;

	int32_t ret = self_gen->m_dtype->getDeviceName(deviceName);
	if (ret) {
		PyErr_SetObject(PyExc_RuntimeError, adsErrorStr(ret));
		return NULL;
	}

	return PyUnicode_FromString(deviceName.c_str());
}