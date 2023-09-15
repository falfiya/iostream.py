# pyiostream

Goals:

- use most of the iostream classes
- doesn't have to be completely true to life
- simplify, best attempt using python
- well commented so that a pythonista could understand it

## std::streambuf

- abstract the device (file, memory, stream)
- place to put or get characters

## std::char_traits

<blockquote>
The char_traits class is a traits class template that abstracts basic character and string operations for a given character type. The defined operation set is such that generic algorithms almost always can be implemented in terms of it. It is thus possible to use such algorithms with almost any possible character or string type, just by supplying a customized char_traits class.

The char_traits class template serves as a basis for explicit instantiations. The user can provide a specialization for any custom character types. Several explicit specializations are provided for the standard character types (see below), other specializations are not required to satisfy the requirements of CharTraits.
</blockquote>

## std::locale

Not implemented.
