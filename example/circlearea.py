# This program will output the circumference and area of the circle with a given radius.

# from iostream import std
import iostream as std

PI: float = 3.14
RADIUS: float = 5.4

area: float = PI * RADIUS * RADIUS
circumference: int = PI * RADIUS * 2

cout << "The circumference of the circle is " << circumference << endl
cout << "The area of the circle is " << area << endl
