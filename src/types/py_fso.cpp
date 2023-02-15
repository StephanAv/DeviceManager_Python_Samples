#include <Python.h>
#include "file_system_object.h"
#include "py_fso.h"
#include "ads_py_error.h"

PyObject* dir(PyObject* self, PyObject* args)
{
    FsoType* self_fso = reinterpret_cast<FsoType*>(self);

    char* path = NULL;
    if (!PyArg_ParseTuple(args, "s", &path)) {
        return NULL;
    }

    std::vector<std::string> folders;
    std::vector<std::string> files;

    int32_t ret = self_fso->m_dtype->dir(path, folders, files);
    if (ret) {
        PyErr_SetObject(PyExc_RuntimeError, adsErrorStr(ret));
        return NULL;
    }

    // Process folders 
    PyObject* pyListFolders = PyList_New(folders.size());

    for (Py_ssize_t i = 0; i < folders.size(); i++) {
            PyObject* pyFolder = PyUnicode_FromString(folders[i].c_str());
            if (!pyFolder) {
                continue;
            }
            PyList_SetItem(pyListFolders, i, pyFolder);
    }

    // Process files
    PyObject* pyListFiles = PyList_New(files.size());

    for (Py_ssize_t j = 0; j < files.size(); j++) {
        PyObject* pyFile = PyUnicode_FromString(files[j].c_str());
        if (!pyFile) {
            continue;
        }
        PyList_SetItem(pyListFiles, j, pyFile);
    }

    return Py_BuildValue("OO", pyListFolders, pyListFiles);
}

PyObject* deleteFile(PyObject* self, PyObject* args)
{
    FsoType* self_fso = reinterpret_cast<FsoType*>(self);

    char* path = NULL;
    int bRecursive = false;

    if (!PyArg_ParseTuple(args, "s|p", &path, &bRecursive)) {
        return NULL;
    }

    int32_t ret = self_fso->m_dtype->deleteFile(path, bRecursive);
    if (ret) {
        PyErr_SetObject(PyExc_RuntimeError, adsErrorStr(ret));
        return NULL;
    }
    Py_RETURN_NONE;
}

PyObject* mkdir(PyObject* self, PyObject* args)
{
    FsoType* self_fso = reinterpret_cast<FsoType*>(self);

    char* path = NULL;
    int bRecursive = false;

    if (!PyArg_ParseTuple(args, "s|p", &path, &bRecursive)) {
        return NULL;
    }

    int32_t ret = self_fso->m_dtype->mkdir(path, bRecursive);
    if (ret) {
        PyErr_SetObject(PyExc_RuntimeError, adsErrorStr(ret));
        return NULL;
    }
    Py_RETURN_NONE;
}

PyObject* readFile(PyObject* self, PyObject* args)
{
    FsoType* self_fso = reinterpret_cast<FsoType*>(self);
    char* targetFilePath = NULL;
    char* localFilePath  = NULL;

    if (!PyArg_ParseTuple(args, "ss", &targetFilePath, &localFilePath)) {
        return NULL;
    }

    std::ofstream fileSink;
    fileSink.exceptions(std::ifstream::badbit);

    try {
        fileSink.open(localFilePath, std::ios::binary);
        int32_t ret = self_fso->m_dtype->readDeviceFile(targetFilePath, fileSink);
        if (ret) {
            PyErr_SetObject(PyExc_RuntimeError, adsErrorStr(ret));
            return NULL;
        }
        fileSink.close();
    }
    catch (const std::ifstream::failure& e) {
        PyErr_SetString(PyExc_IOError, e.what());
        return NULL;
    }
    if (!fileSink) {
        PyErr_SetString(PyExc_IOError, "Writing local file failed");
        return NULL;
    }

    Py_RETURN_NONE;
}

PyObject* writeFile(PyObject* self, PyObject* args)
{
    FsoType* self_fso = reinterpret_cast<FsoType*>(self);

    char* targetFilePath = NULL;
    char* sourceFilePath = NULL;
    if (!PyArg_ParseTuple(args, "ss", &targetFilePath, &sourceFilePath)) {
        return NULL;
    }

    std::ifstream fileSource;
    fileSource.exceptions(std::ifstream::badbit);
    try {
        fileSource.open(sourceFilePath, std::ios::binary);
        int32_t ret = self_fso->m_dtype->writeDeviceFile(targetFilePath, fileSource);
        if (ret) {
            PyErr_SetObject(PyExc_RuntimeError, adsErrorStr(ret));
            return NULL;
        }
        fileSource.close();
    }
    catch (const std::ifstream::failure& e) {
        PyErr_SetString(PyExc_IOError, e.what());
        return NULL;
    }
    if (!fileSource) {
        PyErr_SetString(PyExc_IOError, "Reading from local file failed");
        return NULL;
    }

    Py_RETURN_NONE;
}

PyObject* copyFile(PyObject* self, PyObject* args)
{
    FsoType* self_fso = reinterpret_cast<FsoType*>(self);
    char* source = NULL;
    char* destination = NULL;
    uint32_t flags = 1;
    

    if (!PyArg_ParseTuple(args, "ss|I", &source, &destination, &flags)) {
        return NULL;
    }

    int32_t ret = self_fso->m_dtype->copyDeviceFile(source, destination, flags);
    if (ret) {
        PyErr_SetObject(PyExc_RuntimeError, adsErrorStr(ret));
        return NULL;
    }
    Py_RETURN_NONE;
}