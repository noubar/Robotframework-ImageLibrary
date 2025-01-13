import unittest
import sys
import os
from unittest import TestCase
from unittest import mock
from unittest.mock import patch
import threading
from time import time

# from mock import patch, MagicMock
srcPath = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(srcPath) 
from src.ImageLibrary.modules.errors import KeyboardException
from src.ImageLibrary.modules.interaction.keyboard import Keyboard


class FuncThread(threading.Thread):
    def __init__(self, func, *args):
        super(FuncThread, self).__init__()
        self.args = args
        self.func = func

    def run(self):
        time.sleep(0.25)  # NOTE: BE SURE TO ACCOUNT FOR THIS QUARTER SECOND FOR TIMING TESTS!
        self.func(self.args)

KEYBOARD_KEYS = [
    '\\t', '\\n', '\\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
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
    'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert',
    'junja', 'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
    'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
    'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
    'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
    'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
    'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
    'shift', 'shiftleft', 'shiftright', 'sleep', 'stop', 'subtract', 'tab',
    'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright',
    'yen', 'command', 'option', 'optionleft'
]

class TestKeyboard(TestCase):
    """
    Test every methode under modules.keyboard
    """
    def setUp(self):
        self.mock = mock.MagicMock()
        self.keys = KEYBOARD_KEYS
        self.patcher = mock.patch.dict('sys.modules', {'pyautogui': self.mock})
        self.patcher.start()
        self.module = Keyboard()

    def tearDown(self):
        self.mock.reset_mock()
        self.patcher.stop()

    def test_type_with_text(self):
        """
        TODO Doc
        """
        self.module.type('I am all text')
        self.mock.press.assert_not_called()
        self.mock.typewrite.assert_called_once_with('I am all text')
        self.mock.reset_mock()

        self.module.type('.')
        self.mock.press.assert_called_once_with('.')

    def test_type_with_umlauts(self):
        """
        TODO Doc
        """
        self.module.type('öäöäü')
        self.mock.typewrite.assert_called_once_with('öäöäü')

    def test_type_with_text_and_keys(self):
        """
        TODO Doc
        """
        self.module.type('I love you', 'Key.ENTER')
        self.mock.typewrite.assert_called_once_with('I love you')
        self.mock.press.assert_called_once_with('enter')

    def test_type_with_utf8_keys(self):
        """
        TODO Doc
        """
        self.module.type('key.Tab')
        self.assertEqual(self.mock.typewrite.call_count, 0)
        self.mock.press.assert_called_once_with('tab')
        self.assertEqual(type(self.mock.press.call_args[0][0]),
                          type(str()))

    def test_type_with_keys_down(self):
        """
        TODO Doc
        """
        self.module.type_with_keys_down('hello', 'key.shift')
        self.mock.keyDown.assert_called_once_with('shift')
        self.mock.typewrite.assert_called_once_with('hello')
        self.mock.keyUp.assert_called_once_with('shift')

    def test_type_with_keys_down_with_invalid_keys(self):
        """
        TODO Doc
        """
        expected_msg = ('Invalid keyboard key "enter", valid keyboard keys '
                        f"are:\n{', '.join(self.keys)}")
        with self.assertRaises(KeyboardException) as cm:
            self.module.type_with_keys_down('sometext', 'enter')
        self.assertEqual(str(cm.exception), expected_msg)

    @mock.patch('pyautogui.hotkey', create=True)
    def test_press_combination(self, mock):
        """
        TODO Doc
        """
        self.module.press_combination( 'Key.ctrl', 'A')
        # FuncThread(self.module.press_combination(), 'Key.ctrl', 'A')
        mock.hotkey.assert_called_once_with('ctrl', 'a')
        self.mock.reset_mock()
        for key in self.keys:
            self.module.press_combination(f'Key.{key}')
            self.mock.hotkey.assert_called_once_with(key.lower())
            self.mock.reset_mock()

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestKeyboard("test_type_with_text"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
