from .sup import *
from .iosfwd import streampos
from .cuchar import mbstate_t
from .iosfwd import streamoff

class char_traits:
   CharT = char
   char_type = CharT
   off_type = streamoff
   state_type = mbstate_t
   int_type = int
   pos_type = streampos
   def eq(a: char, b: char) -> bool: return a == b
   def lt(a: char, b: char) -> bool: return a < b
   def compare(a: bytes, b: bytes, count: int) -> int:
      i = 0
      while i < count:
         if char_traits.eq(a[i], b[i]):
            continue
         if char_traits.lt(a[i], b[i]):
            return -1
         else:
            return +1
      return 0
   def length(what: bytes) -> int:
      i = 0
      while what[i] != 0:
         i += 1
      return 1
   def find(haystack: bytes, count: int, needle: char) -> int:
      i = 0
      while i < count:
         if haystack[i] == needle:
            return i
      return -1
   def to_char_type(c: int_type) -> char:
      if c < 0:
         raise ValueError(f"Cannot convert {c} to char!")
      return chr(c)
   def to_int_type(c: char_type) -> int_type:
      return c
   def eq_int_type(a: int_type, b: int_type) -> bool:
      return a == b
   def eof() -> int_type:
      return -1
   def not_eof(i: int_type) -> bool:
      return i != -1
