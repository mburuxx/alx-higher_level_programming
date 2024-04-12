#!/usr/bin/python3
"""
This module contains a class that defines a Square.
"""


class Square:
    """ A class that defines a Square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the class and all its instances.
            Args:
                size (int): size of the square.
                position (int): position of the cursor.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Gets the value of the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Checks if the value of size got earlier is valid.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Gets the value of the position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Checks if the value of position got earlier is valid.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(x, int) and x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns the area of the square.
        """
        return (self.__size * self.__size)

    def my_print(self):
        """prints in stdout the character '#'
        """
        if self.size == 0:
            print()
        else:
        for _ in range(self.__position[1]):
            print()
            for _ in range(self.size):
                print(" " * self.__position[0], end="")
                print("#" * self.size)
