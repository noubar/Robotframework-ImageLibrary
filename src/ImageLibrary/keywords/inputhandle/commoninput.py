import os
from enum import Enum

class Cardinal(Enum):
    """
    Represents diagonal movement directions.
    """
    upperleft = 0
    upperright = 1
    lowerright = 2
    lowerleft = 3

class Orthogonal(Enum):
    """
    Represents straight (horizontal and vertical) movement directions.
    """
    up = 0
    down = 1
    left = 2
    right = 3

class CommonInput:

    @staticmethod
    def validate_int(x, exception:type[Exception]):
        """
        """
        try:
            x = int(x)
        except ValueError as e:
            raise exception(x) from e
        return x

    @staticmethod
    def validate_float(x, exception:type[Exception]):
        """
        """
        try:
            x = float(x)
        except ValueError as e:
            raise exception(x) from e
        return x

    @staticmethod
    def validate_bool(x, exception:type[Exception]):
        """
        """
        try:
            x = bool(x)
        except ValueError as e:
            raise exception(x) from e
        return x

    @staticmethod
    def validate_path_exist(path, exception:type[Exception]):
        """
        """
        path = os.path.abspath(path)
        if not os.path.exists(path):
            raise exception(path)
        return path

    @staticmethod
    def validate_float_between(num,first,second,exception) -> float:
        """
        Validates the given confidence value.
        it should be between first and second.
        else raises given exception.
        """
        both = (first, second)
        first, second = min(both), max(both)
        try:
            num = float(num)
            if not first >= num >= second:
                raise exception(num)
            return num
        except ValueError as e:
            raise exception(num) from e
