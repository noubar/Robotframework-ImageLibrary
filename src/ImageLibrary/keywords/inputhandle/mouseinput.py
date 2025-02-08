from enum import Enum
from .inputerrors import MouseInputException

class Cardinal(Enum):
    upperleft = 0
    upperright = 1
    lowerright = 2
    lowerleft = 3

class Orthogonal(Enum):
    up = 0
    down = 1
    left = 2
    right = 3

class MouseInput:

    @staticmethod
    def validate_button(name):
        """
        Takes a string and returns a string.
        all valid input output examples:
            'left'
            'middle'
            'right' 
        """
        if name.lower() in ['left', 'middle', 'right']:
            return name.lower()
        else:
            raise MouseInputException.ButtonValue(name)

    @staticmethod
    def validate_double_coordinates(coordinates):
        """
        Takes either tuple, list, or dictionary and returns a tuple of integers.
        all valid input output examples:
            ({'x': '100', 'y': '200'}, {'x': '300', 'y': '400'}) to ((100,200), (300,400))
        	(['100', '200'], ['300', '400']) to ((100,200), (300,400))
            ((100, 200), (300, 400)) to ((100,200), (300,400))
            ('100', '200', '300', '400') to ((100,200), (300,400))
            ('100,200', '100,200') to ((100,200), (100,200))
            ('x=100', 'y=200', 'x=300', 'y=400') to ((100,200), (300,400))
        examples are fed to validate_coordinates"""
        if isinstance(coordinates, (list, tuple)):
            coords = ()
            if len(coordinates) == 2:
                coords = (MouseInput.validate_coordinates((coordinates[0],)), MouseInput.validate_coordinates((coordinates[0],)))
            elif len(coordinates) == 4:
                coords = (MouseInput.validate_coordinates(coordinates[:2]), MouseInput.validate_coordinates(coordinates[2:]))
            else:
                raise MouseInputException.CoordinateCount(len(coordinates))
            return coords
        else:
            raise MouseInputException.CoordinateType()

    @staticmethod
    def validate_coordinates(coordinates):
        """
        Takes either tuple of tuple, list, str, or dictionary and returns a tuple of integers.
        all valid input output examples:
        (100,200) to (100,200)
        [100,200] to (100,200)
        ({'x': '400', 'y': '400'},)  to (400,400)
        ('200,200',) to (200,200)
        (['500', '500'],) to (500,500)
        ((300, 300),)  to (300,300)
        ('200', '200') to (200,200)
        ('x=100', 'y=100') to (100,100)
        """
        if isinstance(coordinates, (list, tuple)):
            if len(coordinates) == 1 and isinstance(coordinates[0], (list, tuple, dict, str)):
                coordinates = coordinates[0]
            if isinstance(coordinates, dict):
                try:
                    coordinates = (coordinates['x'], coordinates['y'])
                except KeyError:
                    raise MouseInputException(f'Dictionary must have keys "x" and "y" but given was: {coordinates}') from None
            elif isinstance(coordinates, str):
                print("iam in str")
                coordinates = coordinates.split(',')
            elif len(coordinates) != 2:
                raise MouseInputException.CoordinateCount(len(coordinates))
            elif isinstance(coordinates[0], str) and (coordinates[0].startswith('x=') or coordinates[0].startswith('y=')):
                values = {item.split('=')[0]: int(item.split('=')[1]) for item in coordinates}
                coordinates = (values['x'], values['y'])
            try:
                coordinates = tuple(int(coord) for coord in coordinates)
            except ValueError as e:
                raise MouseInputException(f'Coordinates {coordinates} are not integers') from e
            return coordinates
        else:
            raise MouseInputException.CoordinateType()
