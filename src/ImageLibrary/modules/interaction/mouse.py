import pyautogui as ag
from ..errors import MouseException
from robot.api import logger as LOGGER


class Mouse:
    """
    This class contains keywords for mouse interactions such as clicking, moving, and dragging.
    """
    @staticmethod
    def click_to_the_direction_of(direction, location, offset, clicks, button, interval):
        """
        Clicks at a specified location in a given direction with a specified mouse button.
        Args:
            direction (str): The direction to click towards (e.g., 'up', 'down', 'left', 'right').
            location (tuple): The base location (x, y) from which the direction is calculated.
            offset (int): The offset distance from the base location in the specified direction.
            clicks (int): The number of times to click.
            button (str): The mouse button to use for clicking ('left', 'middle', 'right').
            interval (float): The interval between clicks in seconds.
        Raises:
            MouseException: If `clicks` is not an integer, `button` is not a valid mouse button, 
                            or `interval` is not a float.
        Example:
            click_to_the_direction_of('right', (100, 200), 50, 2, 'left', 0.5)
            # This will click 2 times at the location (150, 200) with the left mouse button 
            # at an interval of 0.5 seconds.
                                   clicks, button, interval):
        """
        x, y = Extras.get_location_according_direction(direction, location, offset)
        try:
            clicks = int(clicks)
        except ValueError as e:
            raise MouseException('Invalid argument "%s" for `clicks`') from e
        if button not in ['left', 'middle', 'right']:
            raise MouseException(f'Invalid button "{button}" for `button`')
        try:
            interval = float(interval)
        except ValueError as e:
            raise MouseException('Invalid argument "%s" for `interval`') from e

        LOGGER.info(f'Clicking {clicks} time(s) at ({x}, {y}) with '
                    f'{button} mouse button at interval {interval}')
        ag.click(x, y, clicks=clicks, button=button, interval=interval)

    @staticmethod
    def move_to(*coordinates, duration=0.0):
        """
        TODO Doc
        """
        coordinates = Extras.validate_cordinates(coordinates)
        ag.moveTo(coordinates, duration=duration)

    @staticmethod
    def up(*coordinates, button):
        """
        TODO Doc
        """
        coordinates = Extras.validate_cordinates(coordinates)
        ag.mouseUp(coordinates, button=button)

    @staticmethod
    def down(*coordinates, button):
        """
        TODO Doc
        """
        coordinates = Extras.validate_cordinates(coordinates)
        ag.mouseDown(coordinates, button=button)

    @staticmethod
    def click(*coordinates, button):
        """
        TODO Doc
        """
        coordinates = Extras.validate_cordinates(coordinates)
        ag.click(*coordinates, button=button)

    @staticmethod
    def double_click(*coordinates, interval, button):
        """
        TODO Doc
        """
        coordinates = Extras.validate_cordinates(coordinates)
        ag.doubleClick(coordinates, interval=interval, button=button)

    @staticmethod
    def triple_click(*coordinates, interval, button):
        """
        TODO Doc
        """
        coordinates = Extras.validate_cordinates(coordinates)
        ag.tripleClick(coordinates, interval=interval, button=button)

    @staticmethod
    def click_hold(*coordinates, time, button):
        """
        TODO Doc
        """
        coordinates = Extras.validate_cordinates(coordinates)
        ag.mouseDown(coordinates, button=button)
        ag.sleep(time)
        ag.mouseUp(button=button)

    @staticmethod
    def drag_and_drop(*coordinates, button, duration=0.0):
        """
        TODO Doc
        """
        coordinates = Extras.validate_double_coordinates(coordinates)
        ag.mouseDown(coordinates[0], button=button)
        ag.moveTo(coordinates[1], duration=duration)
        ag.mouseUp(coordinates[1], button=button)

class Extras:

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
        examples are fed to validate_cordinates"""
        if isinstance(coordinates, (list, tuple)):
            coords = ()
            if len(coordinates) == 2:
                coords = (Extras.validate_cordinates((coordinates[0],)), Extras.validate_cordinates((coordinates[0],)))
            elif len(coordinates) == 4:
                coords = (Extras.validate_cordinates(coordinates[:2]), Extras.validate_cordinates(coordinates[2:]))
            else:
                raise MouseException('Invalid number of coordinates. Please give either pair of (x, y) or pair x, y.')
            return coords
        else:
            raise MouseException('Invalid type of coordinates. Please give either pair of (x, y), [x, y], {"x": x, "y": y}, or "x=value, y=value".')
    
    @staticmethod
    def validate_cordinates(coordinates):
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
                    raise MouseException('Dictionary must have keys "x" and "y"') from None
            elif isinstance(coordinates, str):
                print("iam in str")
                coordinates = coordinates.split(',')
            elif len(coordinates) != 2:
                raise MouseException('Invalid number of coordinates. Please give either (x, y) or x, y.')
            elif isinstance(coordinates[0], str) and (coordinates[0].startswith('x=') or coordinates[0].startswith('y=')):
                values = {item.split('=')[0]: int(item.split('=')[1]) for item in coordinates}
                coordinates = (values['x'], values['y'])
            try:
                coordinates = tuple(int(coord) for coord in coordinates)
            except ValueError as e:
                raise MouseException(f'Coordinates {coordinates} are not integers') from e
            return coordinates
        else:
            raise MouseException('Invalid type of coordinates. Please give either (x, y), [x, y], {"x": x, "y": y}, or "x=value, y=value".')

    @staticmethod
    def get_location_according_direction(direction, location, offset):
        """ 
        Calculate a new location based on the given direction and offset.
        Args:
            direction (str): The direction to move from the current location. 
                             Valid values are 'left', 'up', 'right', 'down'.
            location (tuple): A tuple (x, y) representing the current location.
            offset (int): The distance to move in the specified direction.
        Returns:
            tuple: A tuple (x, y) representing the new location after moving in the specified direction by the given offset.
        """
        x, y = location
        offset = int(offset)
        if direction == 'left':
            x = x - offset
        if direction == 'up':
            y = y - offset
        if direction == 'right':
            x = x + offset
        if direction == 'down':
            y = y + offset
        return x, y
