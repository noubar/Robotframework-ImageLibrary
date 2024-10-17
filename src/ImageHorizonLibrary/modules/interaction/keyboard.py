import pyautogui
from ..errors import KeyboardException


class Keyboard:
    """
    TODO Doc
    """

    @staticmethod
    def press_combination(*keys, pause=0.0):
        """ TODO Doc
        Press given keyboard keys.

        All keyboard keys must be prefixed with ``Key.``.

        Keyboard keys are case-insensitive:

        | Press Combination | KEY.ALT | key.f4 | 
        | Press Combination | kEy.EnD |        |

        [XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        See valid keyboard keys here].
        Performs key down presses on the arguments passed in order, then performs
        key releases in reverse order.

        The effect is that calling hotkey('ctrl', 'shift', 'c') would perform a
        "Ctrl-Shift-C" hotkey/keyboard shortcut press.

        Args:
      key(s) (str): The series of keys to press, in order. This can also be a
        list of key strings to press.
      interval (float, optional): The number of seconds in between each press.
        0.0 by default, for no pause in between presses.

        """
        keys = Keyboard.validate_keys(keys)
        pyautogui.hotkey(*keys, interval=pause)
        return True
    
    @staticmethod
    def convert_to_valid_special_key(key):
        """
        TODO Doc
        """
        key = str(key).lower()
        if key.startswith('key.'):
            key = key.split('key.', 1)[1]
        elif len(key) > 1:
            return None
        if key in pyautogui.KEYBOARD_KEYS:
            return key
        return None

    @staticmethod
    def validate_keys(keys):
        """
        TODO Doc 
        """
        valid_keys = []
        for key in keys:
            valid_key = Keyboard.convert_to_valid_special_key(key)
            if not valid_key:
                raise KeyboardException(f'Invalid keyboard key "{key}", valid '
                                        f"keyboard keys are:\n{', '.join(pyautogui.KEYBOARD_KEYS)}")
            valid_keys.append(valid_key)
        return valid_keys

    @staticmethod
    def type(*keys_or_text):
        """Type text and keyboard keys.

        See valid keyboard keys in `Press Combination`.

        Examples:

        | Type | separated              | Key.ENTER | by linebreak |
        | Type | Submit this with enter | Key.enter |              |
        | Type | key.windows            | notepad   | Key.enter    |
        """
        for key_or_text in keys_or_text:
            key = Keyboard.convert_to_valid_special_key(key_or_text)
            if key:
                pyautogui.press(key)
            else:
                pyautogui.typewrite(key_or_text)

    @staticmethod
    def type_with_keys_down(text, *keys):
        """Press keyboard keys down, then write given text, then release the
        keyboard keys. Which means Press and Hold all given keys and then release them all.

        See valid keyboard keys in `Press Combination`.

        Examples:

        | Type with keys down | write this in caps  | Key.Shift |
        """
        valid_keys = Keyboard.validate_keys(keys)
        for key in valid_keys:
            pyautogui.keyDown(key)
        pyautogui.typewrite(text)
        for key in valid_keys:
            pyautogui.keyUp(key)
