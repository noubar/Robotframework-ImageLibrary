from pyautogui import KEYBOARD_KEYS

class KeyboardInputException(Exception):
    """
    Keybpard input error handler
    """
    @staticmethod
    def KeyInvalid(x):
        return MouseInputException(f"Invalid keyboard key {x},"
                                   f"valid keyboard keys are:\n{', '.join(KEYBOARD_KEYS)}")
    @staticmethod
    def Pause(x):
        return MouseInputException(f"Invalid pause time {x} it should be a float.")

    @staticmethod
    def HoldTime(x):
        return MouseInputException(f"Invalid press and hold time {x} it should be a float.")

    @staticmethod
    def Repeated(x):
        return MouseInputException(f"Invalid value for repeatedly pressing {x} "
                                   "it should be a boolean.")

class MouseInputException(Exception):
    """
    Mouse input error handler
    """
    @staticmethod
    def generic(message):
        return MouseInputException(f"{message}")

    @staticmethod
    def CoordinateType():
        return MouseInputException("Invalid type of coordinates. Please give either "
                            "string x,y or two integers x, y or a tuple of two integers (x, y) "
                            "or a list of two integers [x, y]  or a dic {'x': x, 'y': y} "
                            "or explicit valuse of 'x=value, y=value'.")

    @staticmethod
    def CoordinateCount(x):
        return MouseInputException(f"Invalid number of coordinates: '{x}' "
                                   "Please give either pair of (x, y)")

    @staticmethod
    def ClicksCount(x):
        return MouseInputException(f"Given clicks count '{x}' is invalid; "
                                   "it should be an integer.")

    @staticmethod
    def OffsetValue(x):
        return MouseInputException(f"Given offset '{x}' is invalid; "
                                   "it should be an integer.")

    @staticmethod
    def ScrollAmount(x):
        return MouseInputException(f"Given scroll amount '{x}' is invalid; "
                                   "it should be an integer.")
    @staticmethod
    def ButtonValue(x):
        return MouseInputException(f"Invalid button '{x}'; it should be "
                                   "'left', 'middle', or 'right'.")

    @staticmethod
    def IntervalValue(x):
        return MouseInputException(f"Invalid interval '{x}'; it should be a float.")

    @staticmethod
    def DurationValue(x):
        return MouseInputException(f"Invalid duration '{x}'; it should be a float.")

    @staticmethod
    def HoldTime(x):
        return MouseInputException(f"Invalid hold time '{x}'; it should be a float.")

    @staticmethod
    def InvalidCoordinates(x):
        return MouseInputException(f"Invalid coordinates '{x}'.")
