
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

#define DOC(NAME, VALUE)\
%{\
static char _doc_##NAME[] = VALUE;\
%}

%include doc.i

#define __doc__ pcap_doc


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
  $result = $1;
}

/* let functions take raw python objects */
%typemap(python, in) PyObject * {
  $1 = $input;
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
  DOC(pcapObject_pcap_set,"set pcapObject pcap attribute")
  DOC(pcapObject_pcap_get,"get pcapObject pcap attribute")
  pcap_dumper_t *pcap_dumper;
  DOC(pcapObject_pcap_dumper_set,"set pcapObject pcap_dumper attribute")
  DOC(pcapObject_pcap_dumper_get,"get pcapObject pcap_dumper attribute")
  PyObject *callback;
  DOC(pcapObject_callback_set,"set pcapObject callback attribute")
  DOC(pcapObject_callback_get,"get pcapObject callback attribute")
  %extend {
    pcapObject(void);
    DOC(new_pcapObject,"tbd...")
    ~pcapObject(void);
    DOC(delete_pcapObject,"tbd...")
    void open_live(char *device, int snaplen, int promisc, int to_ms);
    DOC(pcapObject_open_live,"tbd...")
    void open_dead(int linktype, int snaplen);
    DOC(pcapObject_open_dead,"tbd...")
    void open_offline(char *filename);
    DOC(pcapObject_open_offline,"tbd...")
    void dump_open(char *fname);
    DOC(pcapObject_dump_open,"tbd...")
    void setnonblock(int nonblock);
    DOC(pcapObject_setnonblock,"tbd...")
    int getnonblock(void);
    DOC(pcapObject_getnonblock,"tbd...")
    /* maybe change netmask to a bpf_u_32, but need a typemap */
    void setfilter(char *str, int optimize, int netmask);
    DOC(pcapObject_setfilter,"tbd...")
    void loop(int cnt, PyObject *PyObj);
    DOC(pcapObject_loop,"tbd...")
    void dispatch(int cnt, PyObject *PyObj);
    DOC(pcapObject_dispatch,"tbd...")
    PyObject *next(void);
    DOC(pcapObject_next,"tbd...")
    int datalink(void);
    DOC(pcapObject_datalink,"tbd...")
    int snapshot(void);
    DOC(pcapObject_snapshot,"tbd...")
    int is_swapped(void);
    DOC(pcapObject_is_swapped,"tbd...")
    int major_version(void);
    DOC(pcapObject_major_version,"tbd...")
    int minor_version(void);
    DOC(pcapObject_minor_version,"tbd...")
    PyObject *stats(void);
    DOC(pcapObject_stats,"tbd...")
    /* this seems to be broken in libpcap.  it always returns null.  
       it's not very useful anyhow.
    FILE *file(void);
    */
    int fileno(void);
    DOC(pcapObject_fileno,"tbd...")

  }
} pcapObject;


/* functions not associated with a pcapObject instance */
char *lookupdev(void);
DOC(lookupdev,"lookupdev()->string")
PyObject *findalldevs(void);
DOC(findalldevs,"...")
PyObject *lookupnet(char *device);
DOC(lookupnet,"tbd...")
void PythonCallBack(u_char *PyFunc,
                    const struct pcap_pkthdr *header,
                    const u_char *packetdata);
DOC(PythonCallBack,"tbd...")


