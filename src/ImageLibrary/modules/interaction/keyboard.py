import pyautogui
from time import sleep
from ..errors import KeyboardException


class Keyboard:
    """
    Keyboard module provides keywords to interact with the keyboard.
    """

    @staticmethod
    def _convert_to_valid_special_key(key, prefix=False):
        """checks if the key is a valid keyboard key and return it in lowercase
        if prefix is True, remove the 'key.' prefix from the key
        """
        key = str(key).lower()
        if prefix:
            if key.startswith('key.'):
                key = key.split('key.', 1)[1]
            elif len(key) > 1:
                return None
        if key in pyautogui.KEYBOARD_KEYS:
            return key
        return None

    @staticmethod
    def _validate_keys(keys, prefix=False):
        """validates the given keys and returns a list of valid keys
        """
        valid_keys = []
        for key in keys:
            valid_key = Keyboard._convert_to_valid_special_key(key, prefix)
            if not valid_key:
                raise KeyboardException(f'Invalid keyboard key "{key}", valid '
                                        f"keyboard keys are:\n{', '.join(pyautogui.KEYBOARD_KEYS)}")
            valid_keys.append(valid_key)
        return valid_keys

    @staticmethod
    def press_combination(*keys, pause=0.0):
        """Press given keyboard hotkeys.

        All keyboard keys must be prefixed with ``Key.``.

        Keyboard keys are case-insensitive:

        | Press Combination | KEY.ALT | key.f4 | 
        | Press Combination | kEy.EnD |        |

        See valid keyboard keys here:
        ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
        ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
        '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
        'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
        'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
        'browserback', 'browserfavorites', 'browserforward', 'browserhome',
        'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
        'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
        'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
        'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
        'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
        'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
        'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
        'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
        'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
        'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
        'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
        'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
        'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
        'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
        'command', 'option', 'optionleft', 'optionright']

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
        keys = Keyboard._validate_keys(keys)
        pyautogui.hotkey(*keys, interval=pause)
        return True

    @staticmethod
    def press_and_hold(time, *keys):
        """press combination with a pause between each key press

        See valid keyboard keys in `Press Combination`
        This is the difference between press_combination and press_and_hold
        press combination takes also pause time which keeps holding the key for that time and preses the next one without releasing the previous one.
        
        """
        valid_keys = Keyboard._validate_keys(keys)
        for key in valid_keys:
            pyautogui.keyDown(key)
            sleep(time)
            pyautogui.keyUp(key)

    @staticmethod
    def type(*keys_or_text):
        """Type text and keyboard keys.

        See valid keyboard keys in `Press Combination`.

        """
        for key_or_text in keys_or_text:
            key = Keyboard._convert_to_valid_special_key(key_or_text, prefix=True)
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
        valid_keys = Keyboard._validate_keys(keys)
        for key in valid_keys:
            pyautogui.keyDown(key)
        pyautogui.typewrite(text)
        for key in valid_keys:
            pyautogui.keyUp(key)
