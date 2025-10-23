// main.c
#include <Python.h>
#include "helloworld_py.h"
#include <stdio.h>

int main(int argc, char **argv) {
    // Initialize Python runtime
    Py_Initialize();

    // Set sys.argv so scripts that use it don't crash
    wchar_t *python_argv[2];
    python_argv[0] = Py_DecodeLocale(argv[0], NULL);
    python_argv[1] = NULL;
    PySys_SetArgvEx(1, python_argv, 0);

    // Run embedded Python script
    int ret = PyRun_SimpleString((const char *)helloworld_py);
    if (ret != 0) {
        fprintf(stderr, "Python script returned error %d\n", ret);
    }

    // Finalize Python
    Py_Finalize();

    // Free memory allocated by Py_DecodeLocale
    PyMem_RawFree(python_argv[0]);

    return ret;
}
