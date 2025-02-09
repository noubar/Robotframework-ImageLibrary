from ..modules.interaction.mouse import Mouse
from robot.api.deco import keyword
from .inputhandle.mouseinput import MouseInput
from .inputhandle.commoninput import CommonInput, Orthogonal, Cardinal
from .inputhandle.inputerrors import MouseInputException

class MouseKeywords(object):

    def __init__(self):
        self.module = Mouse

    @keyword
    def click_above_of(self, offset, *coordinates, clicks=1,
                              button='left', interval=0.0):
        '''Clicks above the given location by the given offset.

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
        self.module.click_to_direction_of(Orthogonal.up,
                                        CommonInput.validate_int(offset, MouseInputException.OffsetValue),
                                        CommonInput.validate_int(clicks, MouseInputException.ClicksCount),
                                        MouseInput.validate_button(button), 
                                        CommonInput.validate_float(interval, MouseInputException.IntervalValue),
                                        MouseInput.validate_coordinates(coordinates))

    @keyword
    def click_below_of(self, offset, *coordinates, clicks=1,
                              button='left', interval=0.0):
        '''Clicks below the given location by the given offset.

        Example:
        See argument documentation in `Click Above Of`.
        '''
        self.module.click_to_direction_of(Orthogonal.down,
                                        CommonInput.validate_int(offset, MouseInputException.OffsetValue),
                                        CommonInput.validate_int(clicks, MouseInputException.ClicksCount),
                                        MouseInput.validate_button(button), 
                                        CommonInput.validate_float(interval, MouseInputException.IntervalValue),
                                        MouseInput.validate_coordinates(coordinates))

    @keyword
    def click_left_of(self, offset, *coordinates, clicks=1,
                             button='left', interval=0.0):
        '''Clicks left of the given location by the given offset.

        Example:
        See argument documentation in `Click Above Of`.
        '''
        self.module.click_to_direction_of(Orthogonal.left,
                                        CommonInput.validate_int(offset, MouseInputException.OffsetValue),
                                        CommonInput.validate_int(clicks, MouseInputException.ClicksCount),
                                        MouseInput.validate_button(button), 
                                        CommonInput.validate_float(interval, MouseInputException.IntervalValue),
                                        MouseInput.validate_coordinates(coordinates))

    @keyword
    def click_upper_right_of(self, offset, *coordinates, clicks=1,
                              button='left', interval=0.0):
        '''Clicks upper right (North East) of the given location by the given offset.

        Example:
        See argument documentation in `Click Above Of`.
        '''
        self.module.click_to_direction_of(Cardinal.upperright,
                                        CommonInput.validate_int(offset, MouseInputException.OffsetValue),
                                        CommonInput.validate_int(clicks, MouseInputException.ClicksCount),
                                        MouseInput.validate_button(button),
                                        CommonInput.validate_float(interval, MouseInputException.IntervalValue),
                                        MouseInput.validate_coordinates(coordinates))

    @keyword
    def click_upper_left_of(self, offset, *coordinates, clicks=1,
                              button='left', interval=0.0):
        '''Clicks upper left (North West) of the given location by the given offset.

        Example:
        See argument documentation in `Click Above Of`.
        '''
        self.module.click_to_direction_of(Cardinal.upperleft,
                                        CommonInput.validate_int(offset, MouseInputException.OffsetValue),
                                        CommonInput.validate_int(clicks, MouseInputException.ClicksCount),
                                        MouseInput.validate_button(button),
                                        CommonInput.validate_float(interval, MouseInputException.IntervalValue),
                                        MouseInput.validate_coordinates(coordinates))

    @keyword
    def click_lower_right_of(self, offset, *coordinates, clicks=1,
                              button='left', interval=0.0):
        '''Clicks lower right (South East) of the given location by the given offset.

        Example:
        See argument documentation in `Click Above Of`.
        '''
        self.module.click_to_direction_of(Cardinal.lowerright,
                                        CommonInput.validate_int(offset, MouseInputException.OffsetValue),
                                        CommonInput.validate_int(clicks, MouseInputException.ClicksCount),
                                        MouseInput.validate_button(button),
                                        CommonInput.validate_float(interval, MouseInputException.IntervalValue),
                                        MouseInput.validate_coordinates(coordinates))

    @keyword
    def click_lower_left_of(self, offset, *coordinates, clicks=1,
                              button='left', interval=0.0):
        '''Clicks lower left (South West) of the given location by the given offset.

        Example:
        See argument documentation in `Click Above Of`.
        '''
        self.module.click_to_direction_of(Cardinal.lowerleft,
                                        CommonInput.validate_int(offset, MouseInputException.OffsetValue),
                                        CommonInput.validate_int(clicks, MouseInputException.ClicksCount),
                                        MouseInput.validate_button(button),
                                        CommonInput.validate_float(interval, MouseInputException.IntervalValue),
                                        MouseInput.validate_coordinates(coordinates))


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
        self.module.move_to(MouseInput.validate_coordinates(coordinates),
                            CommonInput.validate_float(duration, MouseInputException.DurationValue))

    @keyword
    def mouse_down_to(self, *coordinates, button='left'):
        '''Presses the specified mouse button down.
        Example:
        for all valid coordinates see `Click` keyword
        '''
        self.module.down(MouseInput.validate_coordinates(coordinates),
                        button=MouseInput.validate_button(button))

    @keyword
    def mouse_up_to(self, *coordinates, button='left'):
        '''Releases the specified mouse button.
        Example:
        for all valid coordinates see `Click` keyword
        '''
        self.module.up(MouseInput.validate_coordinates(coordinates),
                       button=MouseInput.validate_button(button))

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
        self.module.click(MouseInput.validate_coordinates(coordinates),
                          button=MouseInput.validate_button(button))

    @keyword
    def click_hold_to(self, time, *coordinates, button='left'):
        '''Clicks and holds the specified mouse button.
        time is the time in seconds to hold the button down.
        Valid buttons are ``left``, ``right`` or ``middle``.
        Example:
            | Click Hold To   | 25 | 150 | 2 |
        for all valid coordinates see `Click` keyword
        '''
        self.module.click_hold(MouseInput.validate_coordinates(coordinates),
                               time=CommonInput.validate_float(time, MouseInputException.HoldTime),
                               button=MouseInput.validate_button(button))

    @keyword
    def double_click_to(self, *coordinates, button='left', interval=0.0):
        '''Double clicks with the specified mouse button.

        See documentation of ``button`` in `Click`.

        ``interval`` specifies the time between clicks and should be
        floating point number.
        for all valid coordinates see `Click` keyword
        '''
        self.module.double_click(MouseInput.validate_coordinates(coordinates),
                            interval=CommonInput.validate_float(interval, MouseInputException.IntervalValue),
                            button=MouseInput.validate_button(button))

    @keyword
    def triple_click_to(self, *coordinates, button='left', interval=0.0):
        '''Triple clicks with the specified mouse button.

        See documentation of ``button`` in `Click`.

        See documentation of ``interval`` in `Double Click`.
        for all valid coordinates see `Click` keyword
        '''
        self.module.triple_click(MouseInput.validate_coordinates(coordinates),
                                interval=float(interval),
                                button=MouseInput.validate_button(button))

    @keyword
    def scroll_to(self, amount, *coordinates):
        '''Sends mouse scroll to the given location either up if the amount is positive
        or down if the amount is negative.

        for all valid coordinates see `Click` keyword
        '''
        self.module.scroll_to(MouseInput.validate_coordinates(coordinates),
                            amount=CommonInput.validate_int(amount, MouseInputException.ScrollAmount))

    @keyword
    def drag_and_drop_to(self, *doublecoordinates, button='left', duration=0.0):
        '''Drags and drops with the specified mouse button.
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
        self.module.drag_and_drop(MouseInput.validate_double_coordinates(doublecoordinates),
                            button=MouseInput.validate_button(button),
                            duration=CommonInput.validate_float(duration, MouseInputException.DurationValue))
