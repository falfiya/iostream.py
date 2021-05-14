from __future__ import annotations
from typing import *
from bitfield_iota import all_set, iota

class ios_base:
   # openmode
   openmode = NewType("openmode", int)
   iota.reset(1)

   app   : openmode = iota()
   binary: openmode = iota()

   in_   : openmode = iota()
   out   : openmode = iota()

   trunc : openmode = iota()
   ate   : openmode = iota()

   __openmask__: openmode = all_set()

   # fmtflags
   fmtflags = NewType("fmtflags", int)
   iota.reset(1)

   dec        : fmtflags = iota()
   oct        : fmtflags = iota()
   hex        : fmtflags = iota()
   basefield  : fmtflags = dec | oct | hex

   left       : fmtflags = iota()
   right      : fmtflags = iota()
   internal   : fmtflags = iota()
   adjustfield: fmtflags = left | right | internal

   scientific : fmtflags = iota()
   fixed      : fmtflags = iota()
   floatfield : scientific | fixed

   boolalpha  : fmtflags = iota()

   showbase   : fmtflags = iota()

   showpoint  : fmtflags = iota()

   showpos    : fmtflags = iota()

   skipws     : fmtflags = iota()

   unitbuf    : fmtflags = iota()

   uppercase  : fmtflags = iota()

   __fmtmask__: fmtflags = all_set()

   # iostate
   iostate = NewType("iostate", int)
   iota.reset(0)

   goodbit: iostate = iota()
   badbit : iostate = iota()
   failbit: iostate = iota()
   eofbit : iostate = iota()

   __statemask__: ios_base = all_set()

   # seekdir
   seekdir = NewType("seekdir", int)
   iota.reset(0)
   beg: seekdir = iota()
   end: seekdir = iota()
   cur: seekdir = iota()

   # other
   streamsize = NewType("streamsize", int)

   def __init__(self):
      self.__openmode__ : ios_base.openmode   = 0
      self.__fmtflags__ : ios_base.fmtflags   = ios_base.skipws | ios_base.dec
      self.__iostate__  : ios_base.iostate    = 0
      self.__seekdir__  : ios_base.seekdir    = 0
      self.__precision__: ios_base.streamsize = 6
      self.__width__    : ios_base.streamsize = 0

   def flags(self, new_flags: Optional[fmtflags] = None) -> fmtflags:
      old_flags = self.__fmtflags__

      if new_flags is not None:
         self.flags = new_flags

      return old_flags

   def setf(self, new_flags: fmtflags, mask: Optional[fmtflags] = None) -> fmtflags:
      old_fmt_flags = self.__fmtflags__

      if mask is None:
         self.__fmtflags__ |= new_flags
      else:
         self.__fmtflags__ = (
            (self.__fmtflags__ & ~mask) | (new_flags & mask & ios_base.__fmtmask__)
         )

      return old_fmt_flags

   def unsetf(self, mask: fmtflags) -> None:
      self.__fmtflags__ &= mask

   def precision(self, new_precision: Optional[streamsize] = None) -> streamsize:
      old_precision = self.__precision__

      if new_precision is not None:
         self.__precision__ = new_precision

      return old_precision

   def width(self, new_width: Optional[streamsize] = None) -> streamsize:
      old_width = self.__width__

      if new_width is not None:
         self.__width__ = new_width

      return old_width

   class failure(SystemError):
      pass

   class Init:
      # i hate this
      __constructor__: Callable[[ios_base.Init], None]

      def __init__(self):
         self.__constructor__(self)

for key in dir(ios_base):
   print(f"ios_base::{key} = {getattr(ios_base, key)}")
