
SWIG=/usr/local/bin/swig
C=gcc -g
PYTHON_INCLUDES=-I/usr/include/python1.5
PCAP_INCLUDES=-I/usr/include/pcap

OBJS= pcap.o exception.o error.o

all: pcapcmodule.so

pcapcmodule.so: pcap_wrap.o $(OBJS)
	$(CC) -shared pcap_wrap.o $(OBJS) -L../libpcap-0.4 -lpcap -o $@
#	$(CC) -shared pcap_wrap.o $(OBJS) -lpcap -o $@

.c.o:
	$(CC) $(CFLAGS) $(PYTHON_INCLUDES) $(PCAP_INCLUDES) -c $<

pcap_wrap.c: pcap.i
	$(SWIG) -python -shadow pcap.i

clean:
	rm -f *.o *.pyc pcap_wrap.* pcapcmodule.so core

