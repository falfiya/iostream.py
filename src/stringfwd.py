from typing import TypeVar, Generic
from _cxxpy import template

CharT = TypeVar("CharT")

@template
class char_traits(Generic[CharT]):
   ...
