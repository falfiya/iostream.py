from typing import *

i: int = 0

def iota() -> int:
   global i

   last_i = i
   i += 1

   return 1 << last_i

def all_set() -> int:
   global i

   all_set = 0
   current_bit = i

   while current_bit != 0:
      all_set <<= 1
      all_set |= 0b1
      current_bit -= 1

   return all_set

def reset(new_i: int) -> None:
   global i
   i = new_i

iota.reset = reset
