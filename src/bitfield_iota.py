from typing import *

T = TypeVar('T')

class bitfield_iota(Generic[T]):
   def __init__(self) -> None:
      self.i = 1

   def __call__(self) -> T:
      self.i <<= 1
      return self.i

   def all(self) -> T:
      return (self.i << 1) - 1

   def __enter__(self):
      return self

   def __exit__(self):
      self.i = 1
