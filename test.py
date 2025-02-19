import unittest
from unittest import mock
import pyautogui
import subprocess
import os
from src.ImageLibrary.modules.recognition.images import RecognizeImage
from src.ImageLibrary.modules.interaction.os import OperatingSystem
from src.ImageLibrary.modules.orchestrer import Orchesterer
from time import sleep


edge_sigma=2.0
edge_low_threshold=0.1
edge_high_threshold=0.3
recognition_timeout=0
platform = Orchesterer.Platform()
defaults = Orchesterer.Defaults(os.path.curdir, "No Operation")
screenshots = Orchesterer.Screenshots(os.path.curdir)
recognitions = Orchesterer.Recognitions(0.9, 'default', edge_sigma, edge_low_threshold, edge_high_threshold,timeout=0)
copy = OperatingSystem(defaults, platform).copy
recognizer = RecognizeImage(defaults, recognitions)

class TestPyAutoGUI(unittest.TestCase):
    def setUp(self):
        # Mock the pyautogui module
        self.mock_pyautogui = mock.Mock()
        self.patcher = mock.patch.dict('sys.modules', {'pyautogui': self.mock_pyautogui})
        self.patcher.start()

    def tearDown(self):
        # Stop patching sys.modules
        self.patcher.stop()

    def test_mouse_move(self):
        # Simulate importing pyautogui in the code under test
        pyautogui.moveTo(100, 200)  # This actually calls self.mock_pyautogui.moveTo
        self.mock_pyautogui.moveTo.assert_called_with(100, 200)

if __name__ == '__main__':
    # unittest.main()
    # process = os.system(f'start {os.path.abspath(r"c:\repos\Robotframework-ImageLibrary\tests\apps\KeyboardTestConsole.exe")}')
    # sleep(4)
    
    recognizer.wait_for(r'c:\repos\Robotframework-ImageLibrary\ss.png',100)