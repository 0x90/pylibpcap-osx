
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

#include <stdlib.h>
#include <pcap.h>

static char errbuf[PCAP_ERRBUF_SIZE];
static int error_code = 0;
static int error_status = 0;

void throw_exception(int err, char *ebuf)
{
  error_code = err;
  error_status=1;

  if (err == -1) {
    strncpy(errbuf, ebuf, PCAP_ERRBUF_SIZE);
    strncat(errbuf, "\n", PCAP_ERRBUF_SIZE);
  } else
    snprintf(errbuf, PCAP_ERRBUF_SIZE, "[Errno %d] %s\n", err, ebuf);
}

void clear_exception(void)
{
        error_status = 0;
}

int check_exception(void)
{
  return error_status;
#if 0
        if (error_status) {
          return error_code;
        }
        else {
          return 0;
        }
#endif
}

char *get_exception_message(void)
{
    if (error_status) {
      return errbuf;
    }
    else return NULL;
}

