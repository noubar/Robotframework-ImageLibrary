from .inputerrors import MouseInputException


class MouseInput:
    """
    A utility class for validating and processing mouse input.
    """

    @staticmethod
    def validate_button(name: str) -> str:
        """
        Validates the given mouse button name.

        Args:
            name (str): The name of the mouse button ('left', 'middle', or 'right').

        Returns:
            str: The validated mouse button name in lowercase.

        Raises:
            MouseInputException: If the provided button name is invalid.
        """
        name = name.lower()
        if name in ['left', 'middle', 'right']:
            return name
        else:
            raise MouseInputException.ButtonValue(name)

    @staticmethod
    def validate_double_coordinates(coordinates):
        """
        Validates and converts different formats of coordinate pairs into a tuple of integer tuples.

        Args:
            coordinates: A tuple, list, dictionary, or string representation of coordinates.

        Returns:
            tuple: A tuple containing two coordinate pairs (x, y).

        Raises:
            MouseInputException: If the input format is invalid.
        
        All Valind Input Output Examples:
            - ({'x': '100', 'y': '200'}, {'x': '300', 'y': '400'}) → ((100,200), (300,400))
            - (['100', '200'], ['300', '400']) → ((100,200), (300,400))
            - ((100, 200), (300, 400)) → ((100,200), (300,400))
            - ('100', '200', '300', '400') → ((100,200), (300,400))
            - ('100,200', '100,200') → ((100,200), (100,200))
            - ('x=100', 'y=200', 'x=300', 'y=400') → ((100,200), (300,400))
        """
        if isinstance(coordinates, (list, tuple)):
            if len(coordinates) == 2:
                return (MouseInput.validate_coordinates(coordinates[0],),
                          MouseInput.validate_coordinates(coordinates[1],))
            elif len(coordinates) == 4:
                return (MouseInput.validate_coordinates(coordinates[:2]),
                          MouseInput.validate_coordinates(coordinates[2:]))
            else:
                raise MouseInputException.CoordinateCount(len(coordinates))
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
                    raise MouseInputException(
                        f'Dictionary must have keys "x" and "y" but given was: {coordinates}') from None
            elif isinstance(coordinates, str):
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
