from __future__ import annotations
from typing import *
from .cuchar import mbstate_t

streamoff  = NewType("streamoff" , int)
streamsize = NewType("streamsize", int)

State = TypeVar("State")

class fpos(Generic[State]):
   def __init__(self, state: State, offset: streamoff):
      self._state  = state
      self._offset = offset

   def state(self, st: Optional[State]) -> Optional[State]:
      if st is None:
         return self._state
      else:
         self._state = st

streampos = fpos[mbstate_t]

class ios_base:
   # openmode
   openmode = NewType("openmode", int)
   # fmtflags
   fmtflags = NewType("fmtflags", int)
   dec        : fmtflags
   oct        : fmtflags
   hex        : fmtflags
   basefield  : fmtflags

   left       : fmtflags
   right      : fmtflags
   internal   : fmtflags
   adjustfield: fmtflags

   scientific : fmtflags
   fixed      : fmtflags
   floatfield : scientific | fixed

   boolalpha  : fmtflags
   showbase   : fmtflags
   showpoint  : fmtflags
   showpos    : fmtflags
   skipws     : fmtflags
   unitbuf    : fmtflags
   uppercase  : fmtflags
   __fmtmask__: fmtflags = all_set()
