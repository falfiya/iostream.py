from __future__ import annotations
from typing import *
from bitfield_iota import iota

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

   # iostate
   iostate = NewType("iostate", int)
   iota.reset(0)

   goodbit: iostate = iota()
   badbit : iostate = iota()
   failbit: iostate = iota()
   eofbit : iostate = iota()

   # seekdir
   seekdir = NewType("seekdir", int)
   iota.reset(0)
   beg: seekdir = iota()
   end: seekdir = iota()
   cur: seekdir = iota()

   def __init__(self):
      self.__openmode__: ios_base.openmode = 0
      self.__fmtflags__: ios_base.fmtflags = 0
      self.__iostate__ : ios_base.iostate  = 0
      self.__seekdir__ : ios_base.seekdir  = 0

   def flags(self, flags: Optional[fmtflags]) -> fmtflags:
      old_flags = self.__fmtflags__

      if flags is not None:
         self.flags = flags

      return old_flags
