from typing import *
T = TypeVar('T')

# steal the type of overload
def typeof(x: T) -> Type[T]: ...
__overload_t = typeof(overload)
