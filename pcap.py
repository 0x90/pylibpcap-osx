# This file was created automatically by SWIG.
import pcapc
class pcapObjectPtr :
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __del__(self):
        if self.thisown == 1 :
            pcapc.delete_pcapObject(self.this)
    def open_live(self,arg0,arg1,arg2,arg3):
        val = pcapc.pcapObject_open_live(self.this,arg0,arg1,arg2,arg3)
        return val
    def open_offline(self,arg0):
        val = pcapc.pcapObject_open_offline(self.this,arg0)
        return val
    def dump_open(self,arg0):
        val = pcapc.pcapObject_dump_open(self.this,arg0)
        return val
    def setnonblock(self,arg0):
        val = pcapc.pcapObject_setnonblock(self.this,arg0)
        return val
    def getnonblock(self):
        val = pcapc.pcapObject_getnonblock(self.this)
        return val
    def setfilter(self,arg0,arg1,arg2):
        val = pcapc.pcapObject_setfilter(self.this,arg0,arg1,arg2)
        return val
    def loop(self,arg0,arg1):
        val = pcapc.pcapObject_loop(self.this,arg0,arg1)
        return val
    def dispatch(self,arg0,arg1):
        val = pcapc.pcapObject_dispatch(self.this,arg0,arg1)
        return val
    def next(self):
        val = pcapc.pcapObject_next(self.this)
        return val
    def datalink(self):
        val = pcapc.pcapObject_datalink(self.this)
        return val
    def snapshot(self):
        val = pcapc.pcapObject_snapshot(self.this)
        return val
    def is_swapped(self):
        val = pcapc.pcapObject_is_swapped(self.this)
        return val
    def major_version(self):
        val = pcapc.pcapObject_major_version(self.this)
        return val
    def minor_version(self):
        val = pcapc.pcapObject_minor_version(self.this)
        return val
    def stats(self):
        val = pcapc.pcapObject_stats(self.this)
        return val
    def fileno(self):
        val = pcapc.pcapObject_fileno(self.this)
        return val
    def __setattr__(self,name,value):
        if name == "pcap" :
            pcapc.pcapObject_pcap_set(self.this,value)
            return
        if name == "pcap_dumper" :
            pcapc.pcapObject_pcap_dumper_set(self.this,value)
            return
        if name == "callback" :
            pcapc.pcapObject_callback_set(self.this,value)
            return
        self.__dict__[name] = value
    def __getattr__(self,name):
        if name == "pcap" : 
            return pcapc.pcapObject_pcap_get(self.this)
        if name == "pcap_dumper" : 
            return pcapc.pcapObject_pcap_dumper_get(self.this)
        if name == "callback" : 
            return pcapc.pcapObject_callback_get(self.this)
        raise AttributeError,name
    def __repr__(self):
        return "<C pcapObject instance>"
class pcapObject(pcapObjectPtr):
    def __init__(self) :
        self.this = pcapc.new_pcapObject()
        self.thisown = 1






#-------------- FUNCTION WRAPPERS ------------------

lookupdev = pcapc.lookupdev

lookupnet = pcapc.lookupnet

PythonCallBack = pcapc.PythonCallBack



#-------------- VARIABLE WRAPPERS ------------------

