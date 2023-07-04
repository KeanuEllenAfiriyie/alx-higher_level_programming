#!/usr/bin/python3
"""
A module with a Rectangle that does nothing
"""


class Rectangle:
    """
    An empty Rectangle class
    """

    def __init__(self, width=0, height=0):
        """
        Checks the parameters and initializes some values
        Args:
            width (:obj:`int`, optioh of the Rectangle.
            height (:obj:`int`, optional): The height of the Rectangle.
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Returns the widtangle
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        Checks the parameters and set the size of the Rectangle
        Args:
            value (int): The width of the Rectangle.
        Raises:
            TypeError: Ilue` type is not `int`.
            ValueError: If `value` is less than `0`.
        """

        self.__check_valid_width(value)
        self.__width = value

    @property
    def height(self):
        """
        Returns the width of the Rectangle
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        Checks the parameters and set the size of the Rectangle
        Args:
            value (int): Th the Rectangle.
        Raises:
            TypeError: If `value` type is not `int`.
            ValueError: If `value` is less than `0`.
        """

        self.__check_valid_height(value)
        self.__height = value

    def __check_valid_width(self, width):
        """
        Checks if the width is a valid integer
        Args:
            width (ihe Rectangle.
        Raises:
            TypeError: If `width` type is not `int`.
            ValueError: If `width` is less than `0`.
        """

        if self.__check_int_value(width) is False:
            raise TypeError('width must be an integer')

        if self.__check_positive_value(width) is False:
            raise ValueError('width must be >= 0')

    def __check_valid_height(self, height):
        """
        Checks if the height is a valid integer
        Args:
            height (int): The height of the Rectangle.
        Raises:
            TypeError: If ot `int`.
            ValueError: If `height` is less than `0`.
        """

        if self.__check_int_value(height) is False:
            raise TypeError('height must be an integer')

        if self.__check_positive_value(height) is False:
            raise ValueError('height must be >= 0')

    def __check_int_value(self, value):
        """
        Checks if the value is an integer
        Args:
            value (int): The number to verify
        Returns:
            int: If iise.
        """

        if type(value) is int:
            return True

        return False

    def __check_positive_value(self, value):
        """
        Checks if the value is a positive integer
        Args:
            value (int): The number to verify
        Returns:
            int: `True` Ireater than
            or equal to 0, `False` otherwise.
        """

        if value >= 0:
            return True

        return False

    def area(self):
        """
        Computes the aregle.
        Returns:
            int: The area of a Rectangle.
        """

        return self.__width * self.__height

    def perimeter(self):
        """
        Computes the Rectangle.
        Returns:
            int: The perimeter of a Rectangle.
        """

        if self.__width == 0 or self.__height == 0:
            return 0

        return self.__width * 2 + self.__height * 2
