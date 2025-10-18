#include <Python.h>

// #include "generated_inittab_modules.h"
#include "generated_inittab_entries.h"

// extern "C" {
//   PyMODINIT_FUNC PyInit_staticmod(void);
// }

int main(int argc, char *argv[]) {
  PyStatus status;
  PyConfig config;
  PyConfig_InitPythonConfig(&config);
  status = PyConfig_SetBytesString(&config, &config.program_name, argv[0]);
  if (PyStatus_Exception(status)) {
    return 1;
  }
  status = PyConfig_SetBytesArgv(&config, argc, argv);
  if (PyStatus_Exception(status)) {
    return 1;
  }
  status = PyConfig_Read(&config);
  if (PyStatus_Exception(status)) {
    return 1;
  }

  // PyImport_AppendInittab("staticmod", PyInit_staticmod);

  // Register all generated modules from the array
  for (const InittabEntry* entry = generated_inittab_extensions; entry->name != NULL; ++entry) {
    PyImport_AppendInittab(entry->name, entry->init_func);
  }

  status = Py_InitializeFromConfig(&config);
  if (PyStatus_Exception(status)) {
    return 1;
  }
  PyConfig_Clear(&config);

  return Py_RunMain();
}
