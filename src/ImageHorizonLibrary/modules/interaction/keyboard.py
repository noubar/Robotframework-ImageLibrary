import pyautogui as ag
from ..errors import KeyboardException


class Keyboard:
    """
    TODO Doc
    """
    @staticmethod
    def press( *keys, **options):
        keys = Keyboard.validate_keys(keys)
        ag.hotkey(*keys, **options)
        return True

    @staticmethod
    def convert_to_valid_special_key( key):
        key = str(key).lower()
        if key.startswith('key.'):
            key = key.split('key.', 1)[1]
        elif len(key) > 1:
            return None
        if key in ag.KEYBOARD_KEYS:
            return key
        return None

    @staticmethod
    def validate_keys( keys):
        valid_keys = []
        for key in keys:
            valid_key = Keyboard.convert_to_valid_special_key(key)
            if not valid_key:
                raise KeyboardException('Invalid keyboard key "%s", valid '
                                        'keyboard keys are:\n%r' %
                                        (key, ', '.join(ag.KEYBOARD_KEYS)))
            valid_keys.append(valid_key)
        return valid_keys
