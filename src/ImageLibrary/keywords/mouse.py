# -*- coding: utf-8 -*-
from ..modules.interaction.mouse import Mouse
from robot.api.deco import keyword

class MouseKeywords(object):

    def __init__(self):
        self.module = Mouse

    @keyword
    def click_above_of(self, offset, *coordinates, clicks=1,
                              button='left', interval=0.0):
        '''Clicks above of given location by given offset.

        ``coordinates`` can be any Python sequence type (tuple, list, etc.) that
        represents coordinates on the screen ie. have an x-value and y-value.
        Locating-related keywords return location you can use with this
        keyword.

        ``offset`` is the number of pixels from the specified ``location``.

        ``clicks`` is how many times the mouse button is clicked.

        See `Click` for documentation for valid coordinates or buttons.

        Example:

        | ${image location}= | Locate | my image | |
        | Click Above Of | 50 | ${image location} |
        | @{coordinates}= | Create List | ${600} | ${500} |
        | Click Above Of | 100 | ${coordinates} | |
        '''
        self.module.click_to_direction_of('up', offset,
                                        clicks, button, interval, *coordinates)

    @keyword
    def click_below_of(self, offset, *coordinates, clicks=1,
                              button='left', interval=0.0):
        '''Clicks below of given location by given offset.

        Example:
        See argument documentation in `Click Above Of`.
        '''
        self.module.click_to_direction_of('down', offset,
                                        clicks, button, interval, *coordinates)

    @keyword
    def click_left_of(self, offset, *coordinates, clicks=1,
                             button='left', interval=0.0):
        '''Clicks left of given location by given offset.

        Example:
        See argument documentation in `Click Above Of`.
        '''
        self.module.click_to_direction_of('left', offset,
                                        clicks, button, interval, *coordinates)

    @keyword
    def click_right_of(self, offset, *coordinates, clicks=1,
                              button='left', interval=0.0):
        '''Clicks right of given location by given offset.

        Example:
        See argument documentation in `Click Above Of`.
        '''
        self.module.click_to_direction_of('right', offset,
                                        clicks, button, interval, *coordinates)

    @keyword
    def move_to(self, *coordinates, duration=0.0):
        '''Moves the mouse pointer to an absolute coordinates.

        ``coordinates`` can either be a Python sequence type with two values
        (eg. ``(x, y)``) or separate values ``x`` and ``y``:

        Example:
        | Move To         | 25             | 150       |     |
        | @{coordinates}= | Create List    | 25        | 150 |
        | Move To         | ${coordinates} |           |     |
        | ${coords}=      | Evaluate       | (25, 150) |     |
        | Move To         | ${coords}      |           |     |

        X grows from left to right and Y grows from top to bottom, which means
        that top left corner of the screen is (0, 0)
        for all valid coordinates see `Click` keyword
        '''
        self.module.move_to(*coordinates, duration=duration)

    @keyword
    def mouse_down_to(self, *coordinates, button='left'):
        '''Presses specidied mouse button down
        Example:
        for all valid coordinates see `Click` keyword
        '''
        self.module.down(*coordinates, button=button)

    @keyword
    def mouse_up_to(self, *coordinates, button='left'):
        '''Releases specified mouse button
        Example:
        for all valid coordinates see `Click` keyword
        '''
        self.module.up(*coordinates, button=button)

    @keyword
    def click_to(self, *coordinates, button='left'):
        '''Clicks with the specified mouse button.
        Example:
        | Click         | 25             | 150       |     |

        Valid buttons are ``left``, ``right`` or ``middle``.

        Valid coordinates are:
            |&{a}  |  Create Dictionary    x=100    y=200
            | Click | ${a}  |

            |@{a} | Create List | 100 | 200 |
            | Click | ${a} |

            |${a} | Evaluate | (100,200) |
            | Click | ${a}  |

            | Click | 100 | 200 |

            | Click | x=100 | y=200 |

            | Click | 100,200 |
        '''
        self.module.click(*coordinates, button=button)

    @keyword
    def click_hold_to(self, time, *coordinates, button='left'):
        '''Clicks with the specified mouse button.
        time is the time in seconds to hold the button down.
        Valid buttons are ``left``, ``right`` or ``middle``.
        Example:
            | Click Hold To   | 25 | 150 | 2 |
        for all valid coordinates see `Click` keyword
        '''
        self.module.click_hold(*coordinates, time=time, button=button)

    @keyword
    def drag_and_drop_to(self, *doublecoordinates, button='left', duration=0.0):
        '''Clicks with the specified mouse button.
        time is the time in seconds to hold the button down.
        Valid buttons are ``left``, ``right`` or ``middle``.
        Example:
            | Drag And Drop To | 25 | 150 | 29 | 28 |
            | ${coordsFrom}=   | Evaluate | (25, 150) |
            | ${coordsTo}=     | Evaluate | (25, 150) |
            | Drag And Drop To | ${coordsFrom} | ${coordsTo} | button=right | duration=2 |

        Valid coordinates are:
            | &{a} | Create Dictionary | x=100 | y=200 |
            | &{b} | Create Dictionary | x=300 | y=400 |
            | Drag And Drop To | ${a} | ${b} |

            | @{a} | Create List | 100 | 20 |
            | @{b} | Create List | 300 | 40 |
            | Drag And Drop To | ${a} | ${b} |

            | ${a} | Evaluate | (100,200) |
            | ${b} | Evaluate | (300,400) |
            | Drag And Drop To | ${a} | ${b} |

            | Drag And Drop To | 100 | 200 | 300 | 400 |

            | Drag And Drop To | 100,200 | 100,200 |

            | Drag And Drop To | x=100 | y=200 | x=300 | y=400 |
        '''
        self.module.drag_and_drop(*doublecoordinates, button=button, duration=duration)

    @keyword
    def double_click_to(self, *coordinates, button='left', interval=0.0):
        '''Double clicks with the specified mouse button.

        See documentation of ``button`` in `Click`.

        ``interval`` specifies the time between clicks and should be
        floating point number.
        for all valid coordinates see `Click` keyword
        '''
        self.module.double_click(*coordinates, interval=float(interval), button=button)

    @keyword
    def triple_click_to(self, *coordinates, button='left', interval=0.0):
        '''Triple clicks with the specified mouse button.

        See documentation of ``button`` in `Click`.

        See documentation of ``interval`` in `Double Click`.
        for all valid coordinates see `Click` keyword
        '''
        self.module.triple_click(*coordinates, interval=float(interval), button=button)

    @keyword
    def scroll_to(self, amount, *coordinates):
        '''sends mouse scroll to the given location either up if amount is positive
        or down if the amount is negative.

        for all valid coordinates see `Click` keyword
        '''
        self.module.scroll_to(*coordinates, amount=amount)
