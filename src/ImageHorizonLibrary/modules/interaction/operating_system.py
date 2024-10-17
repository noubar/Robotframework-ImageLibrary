from modules.interaction.keyboard import Keyboard
import pyautogui as ag
from ..utils import is_mac
from tkinter import Tk as TK

class OperatingSystem:
    """
    TODO Doc
    """
    class _tk:
        def __init__(self):
            self.tk = TK()

        def __enter__(self):
            yield self.tk.clipboard_get()

        def __exit__(self, *exc):
            self.tk.destroy()

    def __init__(self,orchesterer):
        self.orchesterer = orchesterer

    def copy(self):
        """Executes ``Ctrl+C`` on Windows and Linux, ``⌘+C`` on OS X and
        returns the content of the clipboard."""
        key = 'Key.command' if self.orchesterer.is_mac else 'Key.ctrl'
        Keyboard.press(key, 'c')
        return OperatingSystem.get_clipboard_content()

    @staticmethod
    def get_clipboard_content():
        """Returns what is currently copied in the system clipboard."""
        with OperatingSystem._tk() as clipboard_content:
            return clipboard_content

    @staticmethod
    def pause():
        """Shows a dialog that must be dismissed with manually clicking.

        This is mainly for when you are developing the test case and want to
        stop the test execution.

        It should probably not be used otherwise.
        """
        ag.alert(text='Test execution paused.', title='Pause',
                 button='Continue')
