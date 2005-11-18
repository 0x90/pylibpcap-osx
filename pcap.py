# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _pcap

def _swig_setattr(self,class_type,name,value):
    if (name == "this"):
        if isinstance(value, class_type):
            self.__dict__[name] = value.this
            if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
            del value.thisown
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    self.__dict__[name] = value

def _swig_getattr(self,class_type,name):
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


__doc__ = _pcap.__doc__
for dltname, dltvalue in _pcap.DLT.items():
  globals()[dltname] = dltvalue


class pcapObject(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, pcapObject, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, pcapObject, name)
    def __repr__(self):
        return "<C pcapObject instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, pcapObject, 'this', _pcap.new_pcapObject(*args))
        _swig_setattr(self, pcapObject, 'thisown', 1)
        import sys
        if sys.version[0]=='2':
          self.datalink.im_func.__doc__ = _pcap.pcapObject_datalink.__doc__
          self.fileno.im_func.__doc__ = _pcap.pcapObject_fileno.__doc__
          self.datalinks.im_func.__doc__ = _pcap.pcapObject_datalinks.__doc__
          self.major_version.im_func.__doc__ = _pcap.pcapObject_major_version.__doc__
          self.minor_version.im_func.__doc__ = _pcap.pcapObject_minor_version.__doc__
          self.stats.im_func.__doc__ = _pcap.pcapObject_stats.__doc__
          self.getnonblock.im_func.__doc__ = _pcap.pcapObject_getnonblock.__doc__
          self.open_live.im_func.__doc__ = _pcap.pcapObject_open_live.__doc__
          self.dispatch.im_func.__doc__ = _pcap.pcapObject_dispatch.__doc__
          self.setnonblock.im_func.__doc__ = _pcap.pcapObject_setnonblock.__doc__
          self.is_swapped.im_func.__doc__ = _pcap.pcapObject_is_swapped.__doc__
          self.open_dead.im_func.__doc__ = _pcap.pcapObject_open_dead.__doc__
          self.dump_open.im_func.__doc__ = _pcap.pcapObject_dump_open.__doc__
          self.next.im_func.__doc__ = _pcap.pcapObject_next.__doc__
          self.open_offline.im_func.__doc__ = _pcap.pcapObject_open_offline.__doc__
          self.snapshot.im_func.__doc__ = _pcap.pcapObject_snapshot.__doc__
          self.loop.im_func.__doc__ = _pcap.pcapObject_loop.__doc__
          self.setfilter.im_func.__doc__ = _pcap.pcapObject_setfilter.__doc__
    def __del__(self, destroy=_pcap.delete_pcapObject):
        try:
            if self.thisown: destroy(self)
        except: pass
    def open_live(*args): return _pcap.pcapObject_open_live(*args)
    def open_dead(*args): return _pcap.pcapObject_open_dead(*args)
    def open_offline(*args): return _pcap.pcapObject_open_offline(*args)
    def dump_open(*args): return _pcap.pcapObject_dump_open(*args)
    def setnonblock(*args): return _pcap.pcapObject_setnonblock(*args)
    def getnonblock(*args): return _pcap.pcapObject_getnonblock(*args)
    def setfilter(*args): return _pcap.pcapObject_setfilter(*args)
    def loop(*args): return _pcap.pcapObject_loop(*args)
    def dispatch(*args): return _pcap.pcapObject_dispatch(*args)
    def next(*args): return _pcap.pcapObject_next(*args)
    def datalink(*args): return _pcap.pcapObject_datalink(*args)
    def datalinks(*args): return _pcap.pcapObject_datalinks(*args)
    def snapshot(*args): return _pcap.pcapObject_snapshot(*args)
    def is_swapped(*args): return _pcap.pcapObject_is_swapped(*args)
    def major_version(*args): return _pcap.pcapObject_major_version(*args)
    def minor_version(*args): return _pcap.pcapObject_minor_version(*args)
    def stats(*args): return _pcap.pcapObject_stats(*args)
    def fileno(*args): return _pcap.pcapObject_fileno(*args)

class pcapObjectPtr(pcapObject):
    def __init__(self, this):
        _swig_setattr(self, pcapObject, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, pcapObject, 'thisown', 0)
        _swig_setattr(self, pcapObject,self.__class__,pcapObject)
_pcap.pcapObject_swigregister(pcapObjectPtr)


lookupdev = _pcap.lookupdev

findalldevs = _pcap.findalldevs

lookupnet = _pcap.lookupnet

aton = _pcap.aton

ntoa = _pcap.ntoa

