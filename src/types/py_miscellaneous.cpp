#include <Python.h>
#include "miscellaneous.h"
#include "py_miscellaneous.h"
#include "ads_py_error.h"

PyObject* reboot(PyObject* self, PyObject* args)
{
	MiscType* self_misc = reinterpret_cast<MiscType*>(self);

	int32_t ret = self_misc->m_dtype->rebootDevice();
    if (ret) {
        PyErr_SetObject(PyExc_RuntimeError, adsErrorStr(ret));
        return NULL;
    }

    Py_RETURN_NONE;
}