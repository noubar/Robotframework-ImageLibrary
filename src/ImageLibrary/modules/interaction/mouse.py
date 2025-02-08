import pyautogui as ag
from robot.api import logger as LOGGER
from ...keywords.inputhandle.mouseinput import Orthogonal, Cardinal

ag.FAILSAFE = False

class Mouse:
    """
    This class contains keywords for mouse interactions such as clicking, moving, and dragging.
    """

    @staticmethod
    def click_to_direction_of(direction, offset, clicks, button, interval, coordinates):
        """
        Clicks at a specified location in a given direction with a specified mouse button.
        Args:
            direction (str): The direction to click towards (e.g., 'up', 'down', 'left', 'right').
            coordinates (tuple): The base location (x, y) from which the direction is calculated.
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
        if isinstance(direction, Orthogonal):
            x, y = Extras.get_location_according_direction(direction, coordinates, offset)
        elif  isinstance(direction, Cardinal):
            x, y = Extras.get_location_according_diagonal_direction(direction, coordinates, offset)
        else:
            raise ValueError("Invalid direction type. Must be Orthogonal or Cardinal -MouseInput.")
        LOGGER.info(f'Clicking {clicks} time(s) at ({x}, {y}) with '
                    f'{button} mouse button at interval {interval}')
        ag.click(x, y, clicks=clicks, button=button, interval=interval)


    @staticmethod
    def move_to(*coordinates, duration=0.0):
        """
        TODO Doc
        """
        ag.moveTo(coordinates, duration=duration)

    @staticmethod
    def up(*coordinates, button):
        """
        TODO Doc
        """
        ag.mouseUp(coordinates, button=button)

    @staticmethod
    def down(*coordinates, button):
        """
        TODO Doc
        """
        ag.mouseDown(coordinates, button=button)

    @staticmethod
    def click(*coordinates, button):
        """
        TODO Doc
        """
        ag.click(*coordinates, button=button)

    @staticmethod
    def double_click(*coordinates, interval, button):
        """
        TODO Doc
        """
        ag.doubleClick(coordinates, interval=interval, button=button)

    @staticmethod
    def triple_click(*coordinates, interval, button):
        """
        TODO Doc
        """
        ag.tripleClick(coordinates, interval=interval, button=button)

    @staticmethod
    def click_hold(*coordinates, time, button):
        """
        TODO Doc
        """
        ag.mouseDown(coordinates, button=button)
        ag.sleep(time)
        ag.mouseUp(button=button)

    @staticmethod
    def drag_and_drop(*coordinates, button, duration=0.0):
        """
        TODO Doc
        """
        ag.mouseDown(coordinates[0], button=button)
        ag.moveTo(coordinates[1], duration=duration)
        ag.mouseUp(coordinates[1], button=button)

    @staticmethod
    def scroll_to(*coordinates, amount):
        """
        TODO Doc
        """
        ag.scroll(amount, coordinates[0], coordinates[1])


class Extras:

    @staticmethod
    def get_location_according_direction(direction:Orthogonal, location, offset):
        """ 
        Calculate a new location based on the given direction and offset.
        Args:
            direction (str): The direction to move from the current location. 
                             Valid values are 'left', 'up', 'right', 'down'.
            location (tuple): A tuple (x, y) representing the current location.
            offset (int): The distance to move in the specified direction.
        Returns:
            tuple: A tuple (x, y) representing the new location after 
            moving in the specified direction by the given offset.
        """
        x, y = location
        offset = int(offset)
        if direction == Orthogonal.left:
            x -= offset
        elif direction == Orthogonal.up:
            y -= offset
        elif direction == Orthogonal.right:
            x += offset
        elif direction == Orthogonal.down:
            y += offset
        return x, y

    @staticmethod
    def get_location_according_diagonal_direction(direction:Cardinal, location, offset):
        """ 
        Calculate a new location based on the given diagonal direction and offset.
        Args:
            direction (Extras.Cardinal): The diagonal direction to move from the current location.
            location (tuple): A tuple (x, y) representing the current location.
            offset (int): The distance to move in the specified direction.
        Returns:
            tuple: A tuple (x, y) representing the new location after 
            moving in the specified direction by the given offset.
        """
        x, y = location
        offset = int(offset)
        if direction == Cardinal.upperleft:
            x -= offset
            y += offset
        elif direction == Cardinal.upperright:
            x += offset
            y += offset
        elif direction == Cardinal.lowerright:
            x += offset
            y -= offset
        elif direction == Cardinal.lowerleft:
            x -= offset
            y -= offset
        return x, y
