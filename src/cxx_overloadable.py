from typing import *
from inspect import currentframe
from .type_traits import typeof

__overload_t = typeof(overload)

class OverloadError(SystemError): ...

def cxx_overloadable(_: Any) -> None:
   __lookup__ = {}
   def resolve(*args):
      return __lookup__[tuple(args)]
   resolve.__lookup__ = __lookup__
   resolve.__is_overloadable__ = True
   return resolve

def cxx_overload(args: Any, ret: Any) -> __overload_t:
   def decorate(fn: Callable):
      try:
         resolver = currentframe().f_back.f_locals[fn.__name__]
         getattr(resolver, "__is_overloadable__")
         resolver.__lookup__[tuple(args)] = ret
         return resolver
      except:
         raise OverloadError(f"Could not overload {fn.__name__}!")
   return decorate
