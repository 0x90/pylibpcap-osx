
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


#include <Python.h>
#include <pcap.h>
#include <errno.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include "pypcap.h"

static char ebuf[PCAP_ERRBUF_SIZE];
#if 0
/* this was required with LBL libpcap but is evidently not required with
   or even present in the new libpcap that comes with RH 7.2
 */
void linux_restore_ifr(void);
#endif


static int check_ctx(pcapObject *self);


static int check_ctx(pcapObject *self)
{
  if (!self->pcap) {
    throw_exception(-1,
                    "pcapObject must be initialized via open_live(), "
                    "open_offline(), or open_dead() methods");
    return 1;
  }
  return 0;
}

/*
pcapObject *new_pcapObject(char *device, int snaplen, int promisc, int to_ms)
*/
pcapObject *new_pcapObject(void)
{
  pcapObject *self;

  self = (pcapObject *)malloc(sizeof(pcapObject));
  self->pcap = NULL;
  self->pcap_dumper=NULL;
  self->callback=NULL;

  return self;
}

void delete_pcapObject(pcapObject *self)
{
  if (self->pcap_dumper)
    pcap_dump_close(self->pcap_dumper);
  if (self->pcap)
    pcap_close(self->pcap);
#if 0
#ifdef __linux
  linux_restore_ifr();
#endif
#endif

  free(self);
}


void pcapObject_open_live(pcapObject *self, char *device, int snaplen,
                          int promisc, int to_ms)
{
  self->pcap = pcap_open_live(device, snaplen, promisc, to_ms, ebuf);

  if (!self->pcap)
    throw_exception(1, "pcap_open_live");
}

void pcapObject_open_dead(pcapObject *self, int linktype, int snaplen)
{
  self->pcap = pcap_open_dead(linktype, snaplen);

  if (!self->pcap)
    throw_exception(1, "pcap_open_dead");
}


void pcapObject_open_offline(pcapObject *self, char *fname)
{
  self->pcap = pcap_open_offline(fname, ebuf);

  if (!self->pcap)
    throw_exception(1, "pcap_open_offline");
}


void pcapObject_dump_open(pcapObject *self, char *fname)
{
  self->pcap_dumper = pcap_dump_open(self->pcap, fname);
  if (!self->pcap_dumper)
    throw_exception(1, "pcap_dump_open");
}


void pcapObject_setnonblock(pcapObject *self, int nonblock)
{
  if (check_ctx(self))
    return;
  if (pcap_setnonblock(self->pcap, nonblock, ebuf)<0)
    throw_exception(1,ebuf);
}

int pcapObject_getnonblock(pcapObject *self)
{
  int status;

  if (check_ctx(self))
    return 0;
  status=pcap_getnonblock(self->pcap, ebuf);
  if (status<0)
    throw_exception(1,ebuf);
  return status;
}



void pcapObject_setfilter(pcapObject *self, char *str,
                          int optimize, int netmask)
{
  struct bpf_program bpfprog;
  int status;

  if (check_ctx(self))
    return;

  status = pcap_compile(self->pcap, &bpfprog, str, optimize, (bpf_u_int32)netmask);
  if (status) {
    throw_exception(status, "pcap_compile");
    return;
  }

  status = pcap_setfilter(self->pcap, &bpfprog);
  if (status) 
    throw_exception(status,"pcap_setfilter");
}


void pcapObject_loop(pcapObject *self, int cnt, PyObject *PyObj)
{
  int status;

  if (check_ctx(self))
    return;

  self->callback=PyObj;
  status=pcap_loop(self->pcap,cnt,PythonCallBack,(u_char *)self);
  if (status<0) 
    throw_exception(status,pcap_geterr(self->pcap));

  /* is this necessary, or is it a memory leak? */
  Py_INCREF(PyObj);

}


void pcapObject_dispatch(pcapObject *self, int cnt, PyObject *PyObj)
{
  int status;

  if (check_ctx(self))
    return;

  self->callback=PyObj;
  status=pcap_dispatch(self->pcap,cnt,PythonCallBack,(u_char *)self);
  if (status<0) 
    throw_exception(status,pcap_geterr(self->pcap));

  /* is this necessary, or is it a memory leak? */
  Py_INCREF(PyObj);
  return;
}


PyObject *pcapObject_next(pcapObject *self)
{
  struct pcap_pkthdr header;
  const unsigned char *buf;
  PyObject *outObject;

  if (check_ctx(self))
    return NULL;

  buf = pcap_next(self->pcap, &header);
  
  outObject = Py_BuildValue("is#f", header.len, buf, header.caplen,
			    header.ts.tv_sec*1.0+header.ts.tv_usec*1.0/1e6);
  return outObject;

}


int pcapObject_datalink(pcapObject *self)
{
  if (check_ctx(self))
    return 0;

  return pcap_datalink(self->pcap);
}




int pcapObject_snapshot(pcapObject *self)
{
  if (check_ctx(self))
    return 0;

  return pcap_snapshot(self->pcap);
}


int pcapObject_is_swapped(pcapObject *self)
{
  if (check_ctx(self))
    return 0;

  return pcap_is_swapped(self->pcap);
}


int pcapObject_major_version(pcapObject *self)
{
  if (check_ctx(self))
    return 0;

  return pcap_major_version(self->pcap);
}


int pcapObject_minor_version(pcapObject *self)
{
  if (check_ctx(self))
    return 0;

  return pcap_minor_version(self->pcap);
}


PyObject *pcapObject_stats(pcapObject *self)
{
  struct pcap_stat pstat;
  PyObject *outTuple;

  if (check_ctx(self))
    return NULL;

  /* pcap_stats always returns 0, no need to check */
  pcap_stats(self->pcap, &pstat);

  outTuple=PyTuple_New(3);

  PyTuple_SetItem(outTuple, 0, Py_BuildValue("i", pstat.ps_recv));
  PyTuple_SetItem(outTuple, 1, Py_BuildValue("i", pstat.ps_drop));
  PyTuple_SetItem(outTuple, 2, Py_BuildValue("i", pstat.ps_ifdrop));

  return outTuple;
}

FILE *pcapObject_file(pcapObject *self)
{

  if (check_ctx(self))
    return NULL;

  return pcap_file(self->pcap);
  
}



int pcapObject_fileno(pcapObject *self)
{
  if (check_ctx(self))
    return 0;

  return pcap_fileno(self->pcap);
}





/* functions that are not methods of pcapObject */

char *lookupdev(void)
{
  char *dev;

  dev = pcap_lookupdev(ebuf);
  if (dev)
    return dev;
  else {
    throw_exception(errno,ebuf);
    return NULL;
  }

}

PyObject *findalldevs(void)
{
  pcap_if_t *if_head, *if_current;
  pcap_addr_t *addr_current;
  PyObject *out, *addrlist, *addrlist2, *tmp;
  struct sockaddr_in *addr;
  int status, i;

  status = pcap_findalldevs(&if_head, ebuf);

  if (status) {
    throw_exception(errno, ebuf);
    pcap_freealldevs(if_head);
    return NULL;
  }

  out = PyList_New(0);
  
  for (if_current = if_head; if_current; if_current = if_current->next) {
    addrlist = PyList_New(0);

    for (addr_current = if_current->addresses; addr_current;\
	   addr_current = addr_current->next) {
      
      addrlist2=PyList_New(0);

      /* addr */

      if (addr_current->addr) {
        if (addr_current->addr->sa_family!=AF_INET) 
          throw_exception(-1,"unknown address family");

        addr=(struct sockaddr_in *)(addr_current->addr);
        PyList_Append(addrlist2,\
		      Py_BuildValue("s", inet_ntoa(addr->sin_addr)));
      }
      else 
        PyList_Append(addrlist2, Py_BuildValue(""));


      /* netmask */

      if (addr_current->netmask) {
        if (addr_current->netmask->sa_family!=AF_INET)
          throw_exception(-1,"unknown address family");
     
	addr=(struct sockaddr_in *)(addr_current->netmask);
        PyList_Append(addrlist2,\
		      Py_BuildValue("s", inet_ntoa(addr->sin_addr)));
      }
      else 
        PyList_Append(addrlist2, Py_BuildValue(""));


      /* broadaddr */

      if (addr_current->broadaddr) {
        if (addr_current->broadaddr->sa_family!=AF_INET)
          throw_exception(-1,"unknown address family");

        addr=(struct sockaddr_in *)(addr_current->broadaddr);
        PyList_Append(addrlist2,\
		      Py_BuildValue("s", inet_ntoa(addr->sin_addr)));
      }
      else 
	PyList_Append(addrlist2, Py_BuildValue(""));
   
      
      /* dstaddr */
      
      if (addr_current->dstaddr) {
        if (addr_current->dstaddr->sa_family!=AF_INET)
          throw_exception(-1,"unknown address family");
      
	addr=(struct sockaddr_in *)(addr_current->dstaddr);
        PyList_Append(addrlist2,\
		      Py_BuildValue("s", inet_ntoa(addr->sin_addr)));
      }
      else 
	PyList_Append(addrlist2, Py_BuildValue(""));
      
      PyList_Append(addrlist, PyList_AsTuple(addrlist2));
      
      /*
	at this stage, each member of addrlist2 has three references
	each
      */

      for (i = 0; i < PyList_Size(addrlist2); i++) {
	Py_DECREF(PyList_GetItem(addrlist2, i));
      }
      
      Py_DECREF(addrlist2);
    }

    tmp = Py_BuildValue("ssNi", 
			 if_current->name,
			 if_current->description,
			 PyList_AsTuple(addrlist),
			 if_current->flags);

    PyList_Append(out, tmp);
    Py_DECREF(tmp);

    /* 
       each member of addrlist has three references
    */

    for (i = 0; i < PyList_Size(addrlist); i++)
      {
	tmp = PyList_GetItem(addrlist, i);
	Py_DECREF(tmp);
      }

    Py_DECREF(addrlist);
  }
  
  pcap_freealldevs(if_head);

  return out;
}

/* warning:  the libpcap that ships with RH 6.2 seems to have a buggy
   pcap_lookupnet */

PyObject *lookupnet(char *device)
{
  bpf_u_int32 net=0, mask=0;
  PyObject *outTuple;
  int status;

  status = pcap_lookupnet(device, &net, &mask, ebuf);

  if (status) {
    throw_exception(errno, ebuf);
    return NULL;
  }

  outTuple=PyTuple_New(2);
  PyTuple_SetItem(outTuple, 0, Py_BuildValue("i", net));
  PyTuple_SetItem(outTuple, 1, Py_BuildValue("i", mask));


  return outTuple;
}

PyObject *aton(char *cp)
{
  PyObject *out;
  struct in_addr addr;
  int status;

  status=inet_aton(cp, &addr);
  if (!status) {
    throw_exception(errno, "inet_aton()");
    return NULL;
  }
  out=PyInt_FromLong(addr.s_addr);
  return out;
  
}

char *ntoa(int addr)
{
  struct in_addr in;
  in.s_addr=addr;
  return inet_ntoa(in);  
}





/*
 * This function matches the prototype of a libpcap callback function.
 * It is passed as the function callback for libpcap.
 */

void PythonCallBack(u_char *PyObj, 
                    const struct pcap_pkthdr *header, 
                    const u_char *packetdata)
{
  pcapObject *self;
  PyObject *func, *arglist;

  self = (pcapObject *)PyObj;

  if (check_ctx(self))
    return;

  if (PyCallable_Check(self->callback)) {
    func = self->callback;
    arglist = Py_BuildValue("is#f", header->len, packetdata, header->caplen,
			    header->ts.tv_sec*1.0+header->ts.tv_usec*1.0/1e6);
    PyObject_CallObject(func, arglist);
    Py_DECREF(arglist);
  }
  else if (self->pcap_dumper) {
    pcap_dump((u_char *)self->pcap_dumper, header, packetdata);
  }
}


