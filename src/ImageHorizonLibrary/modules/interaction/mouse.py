import pyautogui as ag
from ..errors import MouseException
from robot.api import logger as LOGGER


class Mouse:
    """
    TODO Doc 
    """
    @staticmethod
    def click_to_the_direction_of(direction, location, offset,
                                   clicks, button, interval):
        """
        TODO Doc
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
    def move_to(*coordinates):
        """
        TODO Doc
        """
        if len(coordinates) > 2 or (len(coordinates) == 1 and
                                type(coordinates[0]) not in (list, tuple)):
            raise MouseException('Invalid number of coordinates. Please give '
                                 'either (x, y) or x, y.')
        if len(coordinates) == 2:
            coordinates = (coordinates[0], coordinates[1])
        else:
            coordinates = coordinates[0]
        try:
            coordinates = [int(coord) for coord in coordinates]
        except ValueError as e:
            raise MouseException(f'Coordinates {coordinates} are not integers') from e
        ag.moveTo(*coordinates)

class Extras:

    @staticmethod
    def get_location_according_direction(direction, location, offset):
        """ 
        TODO Doc
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
