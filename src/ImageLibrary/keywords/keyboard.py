# -*- coding: utf-8 -*-
from ..modules.interaction.keyboard import Keyboard
from robot.api.deco import keyword

class KeyboardKeywords:
    """
    This keyword calss represents the keyboard keywords.
    Trhrough this class you can use the keyboard interaction within your test cases.

    """
    def __init__(self):
        self.module = Keyboard

    @keyword
    def press_combination(self, *keys):
        """Press given keyboard keys.

        Keyboard keys are case-insensitive:

        | Press Combination | ALT | f4 |
        | Press Combination | EnD |    |

        [https://pyautogui.readthedocs.org/en/latest/keyboard.html#keyboard-keys|
        See valid keyboard keys here].
        """
        self.module.press_combination(*keys)

    @keyword
    def press_keys_and_hold(self, time, *keys):
        """Press given keyboard keys.

        time: hold time in seconds in between each press.
        it keeps each key down for that time, then releases it to press and hold the next key.

        Keyboard keys are case-insensitive:

        | Press Keys And Hold | 1 | Down | Up |
        | Press Keys And Hold | 2 | EnD |

        [https://pyautogui.readthedocs.org/en/latest/keyboard.html#keyboard-keys|
        See valid keyboard keys here].
        """
        self.module.press_and_hold(time, *keys)

    @keyword
    def type(self, *keys_or_text):
        """Type text and keyboard keys.
        
        you need to defferentiate between text and keys by using Key prefix.
        keys are case-insensitive bu text is case-sensitive.

        See valid keyboard keys in `Press Combination`.

        Examples:

        | Type | separated              | Key.ENTER | by linebreak |
        | Type | Submit this with enter | Key.enter |              |
        | Type | key.windows            | notepad   | Key.enter    |
        """
        self.module.type(*keys_or_text)

    @keyword
    def type_with_keys_down(self, text, *keys):
        """Press keyboard keys down, then write given text, then release the
        keyboard keys. Which means Press and Hold all given keys and then release them all.

        See valid keyboard keys in `Press Combination`.

        Examples:

        | Type with keys down | write this in caps  | Key.Shift |
        """
        self.module.type_with_keys_down( text, *keys)
