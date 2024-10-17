# -*- coding: utf-8 -*-
from ..modules.interaction.keyboard import Keyboard
from robot.api.deco import keyword

class KeyboardKeywords:
    """
    This keyword TODO
    """
    def __init__(self):
        self.module = Keyboard

    @keyword
    def press_combination(self, *keys):
        """Press given keyboard keys.

        All keyboard keys must be prefixed with ``Key.``.

        Keyboard keys are case-insensitive:

        | Press Combination | KEY.ALT | key.f4 | 
        | Press Combination | kEy.EnD |        |

        [https://pyautogui.readthedocs.org/en/latest/keyboard.html#keyboard-keys|
        See valid keyboard keys here].
        """
        self.module.press_combination(*keys)


    @keyword
    def press_combination_with_pause(self, time, *keys):
        """Press given keyboard keys.

        All keyboard keys must be prefixed with ``Key.``.
        time: pause time in second in between each press

        Keyboard keys are case-insensitive:

        | Press Combination | KEY.ALT | key.f4 | 
        | Press Combination | kEy.EnD |        |

        [https://pyautogui.readthedocs.org/en/latest/keyboard.html#keyboard-keys|
        See valid keyboard keys here].
        """
        self.module.press_combination(*keys, pause=time)


    @keyword
    def type(self, *keys_or_text):
        """Type text and keyboard keys.

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
