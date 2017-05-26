# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_receiver', [dirname(__file__)])
        except ImportError:
            import _receiver
            return _receiver
        if fp is not None:
            try:
                _mod = imp.load_module('_receiver', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _receiver = swig_import_helper()
    del swig_import_helper
else:
    import _receiver
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0



def wiringPiSetup():
  return _receiver.wiringPiSetup()
wiringPiSetup = _receiver.wiringPiSetup

def diff(*args):
  return _receiver.diff(*args)
diff = _receiver.diff

def receiveProtocol(*args):
  return _receiver.receiveProtocol(*args)
receiveProtocol = _receiver.receiveProtocol

def handleInterrupt():
  return _receiver.handleInterrupt()
handleInterrupt = _receiver.handleInterrupt

def enableReceive():
  return _receiver.enableReceive()
enableReceive = _receiver.enableReceive

def enableReceivePin(*args):
  return _receiver.enableReceivePin(*args)
enableReceivePin = _receiver.enableReceivePin

def available():
  return _receiver.available()
available = _receiver.available

def getReceivedValue():
  return _receiver.getReceivedValue()
getReceivedValue = _receiver.getReceivedValue

def resetAvailable():
  return _receiver.resetAvailable()
resetAvailable = _receiver.resetAvailable

def receive():
  return _receiver.receive()
receive = _receiver.receive
# This file is compatible with both classic and new-style classes.


