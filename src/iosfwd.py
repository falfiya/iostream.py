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
   ...
