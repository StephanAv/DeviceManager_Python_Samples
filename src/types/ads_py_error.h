#ifndef ADS_PY_ERROR_H
#define ADS_PY_ERROR_H
#include <Python.h>
#include <cstdint>
#include <sstream>

static PyObject* adsErrorStr(int16_t err){
    // TODO: Differentiate between the differen types of errors
    // https://infosys.beckhoff.com/content/1031/devicemanager/263043211.html?id=2363184543884076807 
    std::stringstream ss;
    ss << "Error occured: 0x" << std::hex << err;
    std::string str = ss.str();
    return PyUnicode_FromString(str.c_str());
}
#endif