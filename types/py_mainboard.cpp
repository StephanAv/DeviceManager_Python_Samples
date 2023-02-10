#include <Python.h>
#include "mainboard.h"
#include "py_mainboard.h"
#include "ads_py_error.h"

PyObject* Mainboard::serialNumber(PyObject* self, PyObject* args)
{
	MbType* self_mb = reinterpret_cast<MbType*>(self);
	std::string serialNumber;

	int32_t ret = self_mb->m_dtype->getSerialNumber(serialNumber);
	if (ret) {
		PyErr_SetObject(PyExc_RuntimeError, adsErrorStr(ret));
		return NULL;
	}

	return PyUnicode_FromString(serialNumber.c_str());
}

PyObject* Mainboard::getMinTemp(PyObject* self, PyObject* args)
{
	MbType* self_mb = reinterpret_cast<MbType*>(self);

	int32_t minTemp = 0;
	int32_t ret = self_mb->m_dtype->getMinTemp(minTemp);

	if (ret) {
		PyErr_SetObject(PyExc_RuntimeError, adsErrorStr(ret));
		return NULL;
	}

	return PyLong_FromLong(minTemp);
}

PyObject* Mainboard::getMaxTemp(PyObject* self, PyObject* args)
{
	MbType* self_mb = reinterpret_cast<MbType*>(self);

	int32_t maxTemp = 0;
	int32_t ret = self_mb->m_dtype->getMaxTemp(maxTemp);

	if (ret) {
		PyErr_SetObject(PyExc_RuntimeError, adsErrorStr(ret));
		return NULL;
	}

	return PyLong_FromLong(maxTemp);
}

PyObject* Mainboard::getTemp(PyObject* self, PyObject* args)
{
	MbType* self_mb = reinterpret_cast<MbType*>(self);

	int16_t temp = 0;
	int32_t ret = self_mb->m_dtype->getTemp(temp);

	if (ret) {
		PyErr_SetObject(PyExc_RuntimeError, adsErrorStr(ret));
		return NULL;
	}

	return PyLong_FromUnsignedLong(temp);
}