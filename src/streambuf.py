from .sup import *
from .string import char_traits
from .iosfwd import streamsize

class basic_streambuf:
   CharT = char
   Traits = char_traits
   def __init__(self):
      oi = Optional[uint]
      self.in_beg: oi = None
      self.in_cur: oi = None
      self.in_end: oi = None
      self.ot_beg: oi = None
      self.ot_cur: oi = None
      self.ot_end: oi = None
   def setbuf(self, s: bytearray, n: streamsize) -> Self:
      return self
   pubsetbuf = setbuf
