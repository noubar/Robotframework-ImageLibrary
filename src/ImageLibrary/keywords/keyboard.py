# -*- coding: utf-8 -*-
from ..modules.interaction.keyboard import Keyboard
from robot.api.deco import keyword

class KeyboardKeywords:
    """
    This keyword calss represents the keyboard keywords.
    Trhrough this class you can use the keyboard interaction within your test cases.

    press keywords are used to press a single key or a combination of keys or chars.
    type keyword is used to type a string or a combination of keys and strings.

    """
    def __init__(self):
        self.module = Keyboard

    @keyword
    def press_keys(self, *keys, pause=0.0):
        """Press given keyboard keys.
        Keys and chars are only available, you can use `type` keyword for strings.
        Keyboard keys are case-insensitive:

        pause: time in seconds to wait between each key press.

        Examples:
        | Press Keys | EnD |    |
        | Press Keys | ALT | f4 |
        | Press Keys | ctrl | Shift | c | pause=2 |

        [https://pyautogui.readthedocs.org/en/latest/keyboard.html#keyboard-keys|
        See valid keyboard keys here].
        """
        self.module.press_keys(*keys, pause=pause)

    @keyword
    def press_and_hold(self, time, *keys, repeated=True):
        """Presses and holds each given keyboard chars or keys after each other for a given time.

        time: hold time in seconds of each press.
        it keeps each key down for that time, then releases it to press and hold the next key.
        repeated: if True, the key will be repeatedly down until it is released,
        to overcome the following problem of pyautogui:

        NOTE: For some reason, this does not seem to cause key repeats like would
        happen if a keyboard key was held down on a text field.

        Keyboard keys are case-insensitive:

        | Press And Hold | 1 | Down | Up |
        | Press And Hold | 1 | S | W |
        | Press And Hold | 2 | EnD |

        [https://pyautogui.readthedocs.org/en/latest/keyboard.html#keyboard-keys|
        See valid keyboard keys here].
        """
        self.module.press_and_hold(time, *keys, repeated=repeated)

    @keyword
    def press_and_hold_together(self, time, *keys, repeated=True):
        """Presses given all given keyboard chars or keys together for a given time.

        time: hold time in seconds in between each press.
        it keeps each key down for that time, then releases it to press and hold the next key.
        repeated: if True, the key will be repeatedly down until it is released,
        to overcome the following problem of pyautogui:

        NOTE: For some reason, this does not seem to cause key repeats like would
        happen if a keyboard key was held down on a text field.
        Keyboard keys are case-insensitive:

        | Press And Hold | 1 | Down | Up |
        | Press And Hold | 2 | EnD |

        [https://pyautogui.readthedocs.org/en/latest/keyboard.html#keyboard-keys|
        See valid keyboard keys here].
        """
        self.module.press_and_hold_all(time, *keys, repeated=repeated)

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
        keyboard keys. 

        See valid keyboard keys in `Press Combination`.

        Examples:

        | Type with keys down | write this in caps  | Key.Shift |
        | Type with keys down | l | key.ctrl | Key.Shift | 

        """
        self.module.type_with_keys_down(text, *keys)
