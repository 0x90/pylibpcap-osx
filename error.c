
/*
Python libpcap
Copyright (C) 2001, David Margrave
Based PY-libpcap (C) 1998, Aaron L. Rhodes

This program is free software; you can redistribute it and/or
modify it under the terms of the BSD Licence

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
*/

#include <pcap.h>
#include <Python.h>

static PyObject *pcapError;
static PyObject *error_object;

int init_errors(PyObject *d)
{
  int i;

  /* the base class */
  pcapError = PyErr_NewException("pcapc.error", NULL, NULL);
  PyDict_SetItemString(d, "error", pcapError);
  Py_INCREF(pcapError);

  error_object = PyErr_NewException("pcapc.EXCEPTION",pcapError,NULL);
  Py_INCREF(error_object);
  PyDict_SetItemString(d, "EXCEPTION", error_object);

} 

int set_error(int error_code, char *error_message)
{
/*
    PyErr_SetString(PyExc_IOError, error_message);
*/
  PyErr_SetString(error_object, error_message);
}
