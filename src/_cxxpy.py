# templates in python, kinda
from typing import TypeVar, Generic, Type, Callable
from types import BuiltinFunctionType, FunctionType

T = TypeVar('T')

def _global_inject_candidate(fn):
   return callable(fn) and not isinstance(fn, BuiltinFunctionType)

_INJECT_THEN_COMPUTE = "__cxxpy_inject_compute__"
def _global_inject(fn: T, injected: dict) -> T:
   globals = {}
   globals.update(fn.__globals__)
   globals.update(injected)
   cpyfn = FunctionType(
      fn.__code__,
      globals,
      fn.__name__,
      fn.__defaults__,
      fn.__closure__
   )
   if hasattr(fn, _INJECT_THEN_COMPUTE):
      return cpyfn()
   else:
      return cpyfn

def computed(fn: Callable[[], T]) -> T:
   setattr(fn, _INJECT_THEN_COMPUTE, True)
   return fn

def template(cls: T) -> T:
   # specializations: {[args: tuple]: cls[...args]}
   s13s = {}

   def __class_getitem__(args):
      if not isinstance(args, tuple):
         args = (args,)

      if args not in s13s:
         class s12n(cls):
            ...
         s13s[args] = s12n

         name = cls.__name__ + ", ".join(map(str, args))
         s12n.__name__ = name
         s12n.__qualname__ = name

         typeargs = {}
         for i, typearg in enumerate(cls.__parameters__):
            typeargs[typearg.__name__] = args[i]
         s12n.__cxxpy_typeargs__ = typeargs

         for key, potential_method in vars(cls).items():
            if _global_inject_candidate(potential_method):
               setattr(s12n, key, _global_inject(potential_method, typeargs))
      return s13s[args]
   cls.__class_getitem__ = __class_getitem__
   return cls

_NOCOPY = ("__dict__", "__doc__", "__module__", "__weakref__")

def implement(actual):
   def decorator(cls: Type[T]) -> None:
      for key, val in vars(cls).items():
         if key not in _NOCOPY:
            if _global_inject_candidate(val):
               val = _global_inject(val, actual.__cxxpy_typeargs__)
            setattr(actual, key, val)
   return decorator
