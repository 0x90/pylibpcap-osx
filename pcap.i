
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

%module pcap

%{
#include <pcap.h>
#include "pypcap.h"
%}


%init %{
  /* d is the dictionary for the current module */
  init_errors(d);

%}

/* typemaps */

/* let functions return raw python objects */
%typemap(python, out) PyObject * {
  $target = $source;
}

/* let functions take raw python objects */
%typemap(python, in) PyObject * {
  $target = $source;
}




%except (python) {
  int err;
  clear_exception();
  $function
  if ((err = check_exception())) {
    set_error(err, get_exception_message());
    return NULL;
  }
  else if(PyErr_Occurred()) {
    return NULL;
  }
}



typedef struct {
  pcap_t *pcap;
  pcap_dumper_t *pcap_dumper;
  PyObject *callback;
  %addmethods {
/*
    pcapObject(char *device, int snaplen, int promisc, int to_ms);
*/
    pcapObject(void);
    ~pcapObject(void);
    void open_live(char *device, int snaplen, int promisc, int to_ms);
    void open_offline(char *filename);
    void dump_open(char *fname);
    /* maybe change netmask to a bpf_u_32, but need a typemap */
    void setfilter(char *str, int optimize, int netmask);
    void loop(int cnt, PyObject *PyObj);
    int dispatch(int cnt, PyObject *PyObj);
    PyObject *next(void);
    int datalink(void);
    int snapshot(void);
    int is_swapped(void);
    int major_version(void);
    int minor_version(void);
    PyObject *stats(void);
    /* this seems to be broken in libpcap.  it always returns null.  
       it's not very useful anyhow.
    FILE *file(void);
    */
    int fileno(void);

  }
} pcapObject;


/* functions not associated with a pcapObject instance */
char *lookupdev(void);
PyObject *lookupnet(char *device);
void PythonCallBack(u_char *PyFunc,
                    const struct pcap_pkthdr *header,
                    const u_char *packetdata);


