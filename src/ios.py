from __future__ import annotations
from typing import *
from ._cxx_semantics import implement
from ._bitfield_iota import bitfield_iota
from .iosfwd import ios_base

@implement
class ios_base:
   # openmode
   openmode = NewType("openmode", int)
   with bitfield_iota[openmode]() as iota:
      app    = iota()
      binary = iota()

      in_    = iota()
      out    = iota()

      trunc  = iota()
      ate    = iota()

      __openmask__ = iota.all()

   # fmtflags
   fmtflags = NewType("fmtflags", int)
   with bitfield_iota[fmtflags]() as iota:
      dec         = iota()
      oct         = iota()
      hex         = iota()
      basefield   = dec | oct | hex

      left        = iota()
      right       = iota()
      internal    = iota()
      adjustfield = left | right | internal

      scientific  = iota()
      fixed       = iota()
      floatfield  = scientific | fixed

      boolalpha   = iota()
      showbase    = iota()
      showpoint   = iota()
      showpos     = iota()
      skipws      = iota()
      unitbuf     = iota()
      uppercase   = iota()

      __fmtmask__: fmtflags = iota.all()

   # iostate
   iostate = NewType("iostate", int)
   with bitfield_iota[iostate]() as iota:
      goodbit = iota()
      badbit  = iota()
      failbit = iota()
      eofbit  = iota()

      __statemask__: ios_base = iota.all()

   # seekdir
   seekdir = NewType("seekdir", int)
   with bitfield_iota[seekdir]() as iota:
      beg = iota()
      end = iota()
      cur = iota()

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
