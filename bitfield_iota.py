from typing import *

i: int = 0

def iota() -> int:
   global i

   if i == 0:
      i = 1
      return 0

   i <<= 1
   return i >> 1

def reset(new_i: int) -> None:
   global i
   i = new_i

iota.reset = reset
