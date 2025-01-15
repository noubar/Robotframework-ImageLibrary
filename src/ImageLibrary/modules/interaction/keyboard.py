import pyautogui
from time import sleep, time
from ..errors import KeyboardException

class Keyboard:
    """
    Keyboard module provides keywords to interact with the keyboard.
    """

    @staticmethod
    def press_keys(*keys, pause=0.0):
        """Press given keyboard hotkeys (chars or keys).

        pause: time in seconds to wait between each key press
        All keyboard keys must be prefixed with ``Key.``.

        Keyboard keys are case-insensitive:

        See valid keyboard hotkeys here:
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
        valid_keys = Extras.validate_keys(keys)
        pyautogui.hotkey(valid_keys, interval=pause)
        return True

    @staticmethod
    def press_and_hold(timeout, *keys, repeated=True):
        """press combination with a pause between each key press
        This can press any char or key on keyboard
        
        pause: time in seconds to hold each key press

        Use the `Press Combination` key if you want to press and hold all keys together.

        Difference between press_combination and press_and_hold:
        press combination in contrast to press and hold preses each key without releasing the previous one.
        See valid keyboard keys in `Press Combination`
        """
        valid_keys = Extras.validate_keys(keys)
        for key in valid_keys:
            if repeated:
                start_time = time()
                while time() - start_time < float(timeout):
                    pyautogui.keyDown(key)
                pyautogui.keyUp(key)
            else:
                pyautogui.keyDown(key)
                sleep(float(timeout))
                pyautogui.keyUp(key)

    @staticmethod
    def press_and_hold_all(timeout, *keys, repeated=True):
        """press combination all together and hold for given time
        This can press any char or key on keyboard
        
        pause: time in seconds to hold each key press

        Use the `Press Keys` key if you want to press and hold all keys together.

        Difference between press_Keys and press_and_hold:
        press keys in contrast to press and does not hold preses each key without releasing the previous one.
        See valid keyboard keys in `Press Keys`
        """
        valid_keys = Extras.validate_keys(keys)
        print(valid_keys)
        if repeated:
            start_time = time()
            while time() - start_time < float(timeout):
                for key in valid_keys:
                    pyautogui.keyDown(key)
            for key in valid_keys:
                pyautogui.keyUp(key)
        else:
            for key in valid_keys:
                pyautogui.keyDown(key)
            sleep(float(timeout))
            for key in valid_keys:
                pyautogui.keyUp(key)

    @staticmethod
    def type(*keys_or_text):
        """Type text and keyboard keys.

        See valid keyboard keys in `Press Combination`.

        """
        for key_or_text in keys_or_text:
            key = Extras.convert_to_valid_special_key(key_or_text, prefix=True)
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
        valid_keys = Extras.validate_keys(keys,prefix=True)
        for key in valid_keys:
            pyautogui.keyDown(key)
        pyautogui.typewrite(text)
        for key in valid_keys:
            pyautogui.keyUp(key)

class Extras:
    @staticmethod
    def convert_to_valid_special_key(key, prefix=False):
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
    def validate_keys(keys, prefix=False):
        """validates the given keys and returns a list of valid keys
        """
        valid_keys = []
        for key in keys:
            valid_key = Extras.convert_to_valid_special_key(key, prefix)
            if not valid_key:
                raise KeyboardException(f'Invalid keyboard key "{key}", valid '
                                        f"keyboard keys are:\n{', '.join(pyautogui.KEYBOARD_KEYS)}")
            valid_keys.append(valid_key)
        return valid_keys