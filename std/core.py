from typing import *

T = TypeVar('T')

MAGIC_ATTR = "__template_specializations__"

def template(cls: T) -> T:
   s13s = {}
   ori_getitem = cls.__class_getitem__
   setattr(cls, MAGIC_ATTR, s13s)
   def getitem(args):
      if not isinstance(args, tuple):
         args = (args,)
      if args in s13s:
         return s13s[args]
      else:
         return ori_getitem(args)
   cls.__class_getitem__ = getitem
   return cls

def specialize(s12n: T) -> T:
   cls = get_origin(s12n)
   if cls is None:
      raise TypeError("Specialization requires fully specified generic arguments!")

   s13s = getattr(cls, MAGIC_ATTR, None)
   if s13s is None:
      raise TypeError("Cannot specialize non-template class!")

   args = get_args(s12n)
   class specialized(cls):
      def __init_subclass__(self):
         s13s[args] = self
   setattr(specialized, MAGIC_ATTR, None)
   return specialized
