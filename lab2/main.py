from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import math

def main():
    r = Rectangle("синего", 23, 22)
    c = Circle("зеленого", 23)
    s = Square("красного", 23)
    print(r)
    print(c)
    print(s)
    print(math.factorial(12))

if __name__ == "__main__":
    main()