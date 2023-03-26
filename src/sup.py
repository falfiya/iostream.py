from typing import *
from typing_extensions import Self

T = TypeVar('T')

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

class ptr(Generic[T]):
   """
   Pointer with optional type
   """
   _: T
   type: Any

   def __init__(self, obj, attr: str, type = None):
      object.__setattr__(self, "_obj", obj)
      object.__setattr__(self, "_attr", attr)
      object.__setattr__(self, "_type", type)

   def __getattribute__(self, attr: str) -> T:
      if attr == "_":
         return object.__getattribute__(self, "_obj")[object.__getattribute__(self, "_attr")]
      elif attr == "type":
         return object.__getattribute__(self, "_type")
      else:
         raise AttributeError(f'Cannot get "{attr}" on ptr!')

   def __setattr__(self, attr: str, new: T) -> None:
      if attr != "_":
         raise AttributeError(f'Cannot set "{attr}" on ptr!')
      object.__getattribute__(self, "_obj")[object.__getattribute__(self, "_attr")] = new

index = NewType("index", uint)

b = byte(1)
