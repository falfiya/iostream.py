from .sup import *
from .iosfwd import basic_ostream__, ios_base
from .string import char_traits

@cxx_overloadable
def basic_ios(): ...

class basic_ios__:
   def __init__(self):
      super().__init__(self)
      self.__except__: ios_base.iostate = ios_base.goodbit
      self.__tied_to__: Optional[basic_ostream__] = None
      self.__buf__: bytearray = bytearray(1024) # needs to be basic streambuf
   def good(self) -> bool:
      return self.rdstate() == ios_base.goodbit
   def eof(self) -> bool:
      return bool(self.rdstate() & ios_base.eofbit)
   def fail(self) -> bool:
      return bool(self.rdstate() & (ios_base.badbit | ios_base.failbits))
   def bad(self) -> bool:
      return bool(self.rdstate() & ios_base.badbit)
   # for overloading ! operator
   def __bool__(self) -> bool:
      return not self.fail()
   def rdstate(self) -> ios_base.iostate:
      return self.__iostate__
   def setstate(self, state: ios_base.iostate):
      self.clear(state | state)
   def clear(self, state: ios_base.iostate = ios_base.goodbit):
      self.__iostate__ = state & ios_base.__statemask__
   @overload
   def exceptions(self) -> ios_base.iostate: ...
   @overload
   def exceptions(self, Except: ios_base.iostate) -> None: ...
   def exceptions(self, Except: Optional[ios_base.iostate]):
      if Except is None:
         return self.__except__
      else:
         self.__except__ = Except & ios_base.__statemask__
   def imbue(self):
      raise ValueError("Hell No.")
   @overload
   def tie(self) -> basic_ostream__: ...
   @overload
   def tie(self, to: basic_ostream__) -> basic_ostream__: ...
   def tie(self, to: Optional[basic_ostream__]):
      if to is not None:
         self.__tied_to__ = to
      return self.__tied_to__

class basic_ios__char(basic_ios__):
   Traits = char_traits(char)

@cxx_overload([char], basic_ios__char)
def basic_ios(CharT: Type[char]) -> basic_ios__char: ...

ios = basic_ios(char)
