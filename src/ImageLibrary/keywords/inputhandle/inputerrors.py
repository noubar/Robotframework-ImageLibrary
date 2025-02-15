from pyautogui import KEYBOARD_KEYS

class ScreenshotInputException(Exception):
    """
    ScreenshotInputException input error handler
    """
    @staticmethod
    def AllScreensValue(x):
        return ScreenshotInputException(f"Invalid if allscreens value '{x}',"
                                        "it should be boolean.")

class RecognitionInputException(Exception):
    """
    Image Recognition input error handler
    """
    @staticmethod
    def StrategyValue(x):
        return RecognitionInputException(f"Invalid strategy '{x}', valid strategies are: "
                                   "'default' or 'pyautogui', 'edge' or 'skimage'.")

    @staticmethod
    def ConfidenceValue(x):
        return RecognitionInputException(f"Invalid confidence value '{x}' "
                                         "it should be a float number between 0 and 1.")

    @staticmethod
    def SigmaValue(x):
        return RecognitionInputException(f"Invalid confidence value '{x}' "
                                         "it should be a float number between 0 and 1.")

    @staticmethod
    def EdgeSigma(x):
        return RecognitionInputException(f"Invalid skimage edge value '{x}' "
                                         "it should be a float.")

    @staticmethod
    def LowThreshold(x):
        return RecognitionInputException(f"Invalid low threshold edge value '{x}' "
                                         "it should be a float number between 0 and 1.")

    @staticmethod
    def HighThreshold(x):
        return RecognitionInputException(f"Invalid high threshold value '{x}' "
                                         "it should be a float number between 0 and 1.")
    @staticmethod
    def ImageRef(x):
        return RecognitionInputException(f"Invalid image reference Name '{x}', "
                                         "it cannot be found under reference folder.")
    @staticmethod
    def Timeout(x):
        return RecognitionInputException(f"Invalid timeout '{x}', "
                                         "it sould be float.")

class OSInputException(Exception):
    """
    Operating System input error handler
    """
    @staticmethod
    def LaunchPath(x):
        return OSInputException(f"Invalid or non-existance path '{x}' to launch the application.")

    @staticmethod
    def ReferencePath(x):
        return OSInputException(f"Invalid or non-existance path '{x}' to reference folder.")

    @staticmethod
    def ScreenshotPath(x):
        return OSInputException(f"Invalid or non-existance path '{x}' to Screenshot folder.")

class KeyboardInputException(Exception):
    """
    Keyboard input error handler
    """
    @staticmethod
    def KeyInvalid(x):
        return KeyboardInputException(f"Invalid keyboard key {x},"
                                   f"valid keyboard keys are:\n{', '.join(KEYBOARD_KEYS)}")
    @staticmethod
    def Pause(x):
        return KeyboardInputException(f"Invalid pause time {x} it should be a float.")

    @staticmethod
    def HoldTime(x):
        return KeyboardInputException(f"Invalid press and hold time {x} it should be a float.")

    @staticmethod
    def Repeated(x):
        return KeyboardInputException(f"Invalid value for repeatedly pressing {x} "
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
        return MouseInputException("Invalid type of coordinates. Please provide either "
                            "string x,y or two integers x, y or a tuple of two integers (x, y) "
                            "or a list of two integers [x, y] or a dict {'x': x, 'y': y} "
                            "or explicit values of 'x=value, y=value'.")

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
