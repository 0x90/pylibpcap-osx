
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

/* the pcap class */
typedef struct {
  pcap_t *pcap;
  pcap_dumper_t *pcap_dumper;
  PyObject *callback;
} pcapObject;


/* pcapObject methods */
/*
pcapObject *new_pcapObject(char *device, int snaplen, int promisc, int to_ms);
*/
pcapObject *new_pcapObject(void);
void delete_pcapObject(pcapObject *self);
void pcapObject_open_live(pcapObject *self, char *device, int snaplen,
                          int promisc, int to_ms);
void pcapObject_open_offline(pcapObject *self, char *fname);
void pcapObject_dump_open(pcapObject *self, char *fname);
void pcapObject_setnonblock(pcapObject *self, int nonblock);
int pcapObject_getnonblock(pcapObject *self);
void pcapObject_setfilter(pcapObject *self, char *str,
                          int optimize, int netmask);
PyObject *pcapObject_next(pcapObject *self);
void pcapObject_dispatch(pcapObject *self, int cnt, PyObject *PyObj);
void pcapObject_loop(pcapObject *self, int cnt, PyObject *PyObj);
int pcapObject_datalink(pcapObject *self);
int pcapObject_snapshot(pcapObject *self);
int pcapObject_is_swapped(pcapObject *self);
int pcapObject_major_version(pcapObject *self);
int pcapObject_minor_version(pcapObject *self);
PyObject *pcapObject_stats(pcapObject *self);
FILE *pcapObject_file(pcapObject *self);
int pcapObject_fileno(pcapObject *self);



/* functions that are not methods of pcapObject */
char *lookupdev(void);
PyObject *lookupnet(char *device);
void pcapObject_setfilter(pcapObject *self, char *str,
                          int optimize, int netmask);
void PythonCallBack(u_char *PyFunc,
                    const struct pcap_pkthdr *header,
                    const u_char *packetdata);

/* error support fuctions */
void throw_exception(int err, char *ebuf);
void clear_exception(void);
int check_exception(void);
char *get_exception_message(void);

void init_errors(PyObject *d);
void set_error(int error_code, char *error_message);

