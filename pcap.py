# This file was created automatically by SWIG.
import pcapc
class pcapObject:
    __setmethods__ = {}
    for _s in []: __setmethods__.update(_s.__setmethods__)
    def __setattr__(self,name,value):
        if (name == "this"):
            if isinstance(value,pcapObject):
                self.__dict__[name] = value.this
                if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
                del value.thisown
                return
        method = pcapObject.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value

    __getmethods__ = {}
    for _s in []: __getmethods__.update(_s.__getmethods__)
    def __getattr__(self,name):
        method = pcapObject.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name

    __setmethods__["pcap"] = pcapc.pcapObject_pcap_set
    __getmethods__["pcap"] = pcapc.pcapObject_pcap_get
    __setmethods__["pcap_dumper"] = pcapc.pcapObject_pcap_dumper_set
    __getmethods__["pcap_dumper"] = pcapc.pcapObject_pcap_dumper_get
    __setmethods__["callback"] = pcapc.pcapObject_callback_set
    __getmethods__["callback"] = pcapc.pcapObject_callback_get
    def __init__(self,*args):
        self.this = apply(pcapc.new_pcapObject,args)
        self.thisown = 1
        import sys
        if sys.version[0]=='2':
          self.setfilter.__setattr__('__doc__',pcapc.pcapObject_setfilter.__doc__)
          self.loop.__setattr__('__doc__',pcapc.pcapObject_loop.__doc__)
          self.major_version.__setattr__('__doc__',pcapc.pcapObject_major_version.__doc__)
          self.minor_version.__setattr__('__doc__',pcapc.pcapObject_minor_version.__doc__)
          self.open_dead.__setattr__('__doc__',pcapc.pcapObject_open_dead.__doc__)
          self.is_swapped.__setattr__('__doc__',pcapc.pcapObject_is_swapped.__doc__)
          self.dump_open.__setattr__('__doc__',pcapc.pcapObject_dump_open.__doc__)
          self.setnonblock.__setattr__('__doc__',pcapc.pcapObject_setnonblock.__doc__)
          self.dispatch.__setattr__('__doc__',pcapc.pcapObject_dispatch.__doc__)
          self.open_live.__setattr__('__doc__',pcapc.pcapObject_open_live.__doc__)
          self.getnonblock.__setattr__('__doc__',pcapc.pcapObject_getnonblock.__doc__)
          self.snapshot.__setattr__('__doc__',pcapc.pcapObject_snapshot.__doc__)
          self.open_offline.__setattr__('__doc__',pcapc.pcapObject_open_offline.__doc__)
          self.next.__setattr__('__doc__',pcapc.pcapObject_next.__doc__)
          self.stats.__setattr__('__doc__',pcapc.pcapObject_stats.__doc__)
          self.fileno.__setattr__('__doc__',pcapc.pcapObject_fileno.__doc__)
          self.datalink.__setattr__('__doc__',pcapc.pcapObject_datalink.__doc__)
    def __del__(self, destroy= pcapc.delete_pcapObject):
        if getattr(self,'thisown',0):
            destroy(self)
    def open_live(*args): return apply(pcapc.pcapObject_open_live,args)
    def open_dead(*args): return apply(pcapc.pcapObject_open_dead,args)
    def open_offline(*args): return apply(pcapc.pcapObject_open_offline,args)
    def dump_open(*args): return apply(pcapc.pcapObject_dump_open,args)
    def setnonblock(*args): return apply(pcapc.pcapObject_setnonblock,args)
    def getnonblock(*args): return apply(pcapc.pcapObject_getnonblock,args)
    def setfilter(*args): return apply(pcapc.pcapObject_setfilter,args)
    def loop(*args): return apply(pcapc.pcapObject_loop,args)
    def dispatch(*args): return apply(pcapc.pcapObject_dispatch,args)
    def next(*args): return apply(pcapc.pcapObject_next,args)
    def datalink(*args): return apply(pcapc.pcapObject_datalink,args)
    def snapshot(*args): return apply(pcapc.pcapObject_snapshot,args)
    def is_swapped(*args): return apply(pcapc.pcapObject_is_swapped,args)
    def major_version(*args): return apply(pcapc.pcapObject_major_version,args)
    def minor_version(*args): return apply(pcapc.pcapObject_minor_version,args)
    def stats(*args): return apply(pcapc.pcapObject_stats,args)
    def fileno(*args): return apply(pcapc.pcapObject_fileno,args)
    def __repr__(self):
        return "<C pcapObject instance at %s>" % (self.this,)

class pcapObjectPtr(pcapObject):
    def __init__(self,this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = pcapObject
pcapc.pcapObject_swigregister(pcapObjectPtr)
__doc__ = pcapc.__doc__
lookupdev = pcapc.lookupdev

findalldevs = pcapc.findalldevs

lookupnet = pcapc.lookupnet

PythonCallBack = pcapc.PythonCallBack


