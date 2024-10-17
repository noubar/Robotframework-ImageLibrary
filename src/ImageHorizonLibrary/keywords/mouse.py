# -*- coding: utf-8 -*-
import pyautogui as ag
from ..modules.interaction.mouse import Mouse
from robot.api.deco import keyword

class MouseKeywords(object):

    def __init__(self):
        self.module = Mouse

    @keyword
    def click_to_the_above_of(self, location, offset, clicks=1,
                              button='left', interval=0.0):
        '''Clicks above of given location by given offset.

        ``location`` can be any Python sequence type (tuple, list, etc.) that
        represents coordinates on the screen ie. have an x-value and y-value.
        Locating-related keywords return location you can use with this
        keyword.

        ``offset`` is the number of pixels from the specified ``location``.

        ``clicks`` is how many times the mouse button is clicked.

        See `Click` for documentation for valid buttons.

        Example:

        | ${image location}=    | Locate             | my image |        |
        | Click To The Above Of | ${image location}  | 50       |        |
        | @{coordinates}=       | Create List        | ${600}   | ${500} |
        | Click To The Above Of | ${coordinates}     | 100      |        |
        '''
        self.module.click_to_the_direction_of('up', location, offset,
                                        clicks, button, interval)

    @keyword
    def click_to_the_below_of(self, location, offset, clicks=1,
                              button='left', interval=0.0):
        '''Clicks below of given location by given offset.

        See argument documentation in `Click To The Above Of`.
        '''
        self.module.click_to_the_direction_of('down', location, offset,
                                        clicks, button, interval)

    @keyword
    def click_to_the_left_of(self, location, offset, clicks=1,
                             button='left', interval=0.0):
        '''Clicks left of given location by given offset.

        See argument documentation in `Click To The Above Of`.
        '''
        self.module.click_to_the_direction_of('left', location, offset,
                                        clicks, button, interval)

    @keyword
    def click_to_the_right_of(self, location, offset, clicks=1,
                              button='left', interval=0.0):
        '''Clicks right of given location by given offset.

        See argument documentation in `Click To The Above Of`.
        '''
        self.module.click_to_the_direction_of('right', location, offset,
                                        clicks, button, interval)

    @keyword
    def move_to(self, *coordinates):
        '''Moves the mouse pointer to an absolute coordinates.

        ``coordinates`` can either be a Python sequence type with two values
        (eg. ``(x, y)``) or separate values ``x`` and ``y``:

        | Move To         | 25             | 150       |     |
        | @{coordinates}= | Create List    | 25        | 150 |
        | Move To         | ${coordinates} |           |     |
        | ${coords}=      | Evaluate       | (25, 150) |     |
        | Move To         | ${coords}      |           |     |


        X grows from left to right and Y grows from top to bottom, which means
        that top left corner of the screen is (0, 0)
        '''
        self.module.move_to(*coordinates)

    @keyword
    def mouse_down(self, button='left'):
        '''Presses specidied mouse button down'''
        ag.mouseDown(button=button)

    @keyword
    def mouse_up(self, button='left'):
        '''Releases specified mouse button'''
        ag.mouseUp(button=button)

    @keyword
    def click_to(self, x, y, button='left'):
        '''Clicks with the specified mouse button.

        Valid buttons are ``left``, ``right`` or ``middle``.
        '''
        ag.click(x, y, button=button)

    @keyword
    def double_click_to(self, x, y, button='left', interval=0.0):
        '''Double clicks with the specified mouse button.

        See documentation of ``button`` in `Click`.

        ``interval`` specifies the time between clicks and should be
        floating point number.
        '''
        ag.doubleClick(x, y, button=button, interval=float(interval))

    @keyword
    def triple_click_to(self, x, y, button='left', interval=0.0):
        '''Triple clicks with the specified mouse button.

        See documentation of ``button`` in `Click`.

        See documentation of ``interval`` in `Double Click`.
        '''
        ag.tripleClick(x, y, button=button, interval=float(interval))
