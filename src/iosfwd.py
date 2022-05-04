from .sup import *
from .bitfield_iota import bitfield_iota
from .string import char_traits

streamoff = uint
streamsize = uint

StateType = TypeVar("StateType")
class fpos(Generic[StateType]):
   def __init__(self, state: StateType, off: streamoff = 0):
      self.__state: StateType = state
      self.__offset: streamoff = off
   @overload
   def state(self, state: StateType) -> None: ...
   @overload
   def state(self) -> StateType: ...
   def state(self, maybe_state: Optional[StateType]):
      if maybe_state is None:
         return self
      else:
         self.__state = maybe_state
   def __add__(self, off: streamoff) -> Self:
      return fpos(self.state, self.__offset + off)
   def __sub__(self, off: streamoff) -> Self:
      return fpos(self.state, self.__offset - off)
   def __iadd__(self, off: streamoff) -> Self:
      self.__offset += off
      return self
   def __isub__(self, off: streamoff) -> Self:
      self.__offset -= off
      return self
   def __eq__(self, other: Self) -> bool:
      return (True
         and self.__state == other.__state
         and self.__offset == other.__offset)
   def __ne__(self, other: Self) -> bool:
      return not self == other

streampos = fpos[char_traits.state_type]

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

      __statemask__: iostate = iota.all()

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

   class failure(SystemError): ...

class basic_ostream__: ...
