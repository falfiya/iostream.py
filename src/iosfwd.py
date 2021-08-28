from typing import NewType, Generic, TypeVar, Optional
from ._cxxpy import template, computed
from ._stdtype import char
from .cuchar import mbstate_t
from .stringfwd import char_traits

streamoff  = NewType("streamoff" , int)
streamsize = NewType("streamsize", int)

State = TypeVar("State")

@template
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

@template
class ios_base:
   ...

CharT = TypeVar("CharT")

@template
class basic_ios(Generic[CharT]):
   @computed
   def Traits():
      return char_traits[CharT]

@template
class basic_streambuf(Generic[CharT]):
   @computed
   def Traits():
      return char_traits[CharT]

@template
class basic_streambuf(Generic[CharT]):
   @computed
   def Traits():
      return char_traits[CharT]

@template
class basic_istream(Generic[CharT]):
   @computed
   def Traits():
      return char_traits[CharT]

@template
class basic_ostream(Generic[CharT]):
   @computed
   def Traits():
      return char_traits[CharT]

@template
class basic_iostream(Generic[CharT]):
   @computed
   def Traits():
      return char_traits[CharT]

ios       = basic_ios[char]
streambuf = basic_streambuf[char]
istream   = basic_istream[char]
ostream   = basic_ostream[char]
iostream  = basic_iostream[char]
stringbuf = basic_str
