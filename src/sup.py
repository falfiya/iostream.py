from typing import *
from typing_extensions import Self

class byte:
   def __new__(cls, either: Union[bytes, int]) -> Self:
      if isinstance(either, int):
         if 0 <= either <= 0xFF:
            return either
         else:
            raise ValueError(f"{either} is not an unsigned integer below 256!")
      if isinstance(either, bytes):
         if len(either) == 1:
            return either[0]
         else:
            raise ValueError(f"{either} is not a single byte!")

char = NewType("char", byte)

class uint:
   def __new__(cls, idx: int) -> Self:
      if idx < 0:
         raise ValueError(f"{idx} must be a positive integer!")
      return idx

index = NewType("index", uint)

T = TypeVar("T")
