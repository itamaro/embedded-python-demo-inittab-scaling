#ifndef EXTENSION_MODULE_MACRO_H
#define EXTENSION_MODULE_MACRO_H

#include "Python.h"

#define GENERATE_EXTENSION_MODULE(N) \
    static PyObject* inittab_ext_##N##_say_hello(PyObject* self, PyObject* args) { \
        printf("Hello from inittab_ext_" #N "!\n"); \
        Py_RETURN_NONE; \
    } \
    static PyMethodDef inittab_ext_##N##_methods[] = { \
        {"say_hello", inittab_ext_##N##_say_hello, METH_NOARGS, "Says hello from extension module " #N "."}, \
        {NULL, NULL, 0, NULL} \
    }; \
    static PyModuleDef_Slot inittab_ext_##N##_slots[] = { \
        {Py_mod_gil, Py_MOD_GIL_NOT_USED}, \
        {Py_mod_multiple_interpreters, Py_MOD_PER_INTERPRETER_GIL_SUPPORTED}, \
        {0, NULL} \
    }; \
    static struct PyModuleDef inittab_ext_##N##_module = { \
        .m_base = PyModuleDef_HEAD_INIT, \
        .m_name = "inittab_ext_" #N, \
        .m_doc = NULL, \
        .m_size = 0, \
        .m_methods = inittab_ext_##N##_methods, \
        .m_slots = inittab_ext_##N##_slots, \
    }; \
    PyMODINIT_FUNC PyInit_inittab_ext_##N(void) { \
        return PyModuleDef_Init(&inittab_ext_##N##_module); \
    }

#endif // EXTENSION_MODULE_MACRO_H
