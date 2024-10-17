import subprocess
import shlex
from tkinter import Tk as TK
import pyautogui as ag
from .keyboard import Keyboard
from ..errors import OSException,InvalidAlias
from robot.api import logger

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

    def __init__(self, defaults, platform):
        self.defaults = defaults
        self.platform = platform

    def copy(self):
        """Executes ``Ctrl+C`` on Windows and Linux, ``⌘+C`` on OS X and
        returns the content of the clipboard."""
        key = 'Key.command' if self.platform.is_mac else 'Key.ctrl'
        Keyboard.press(key, 'c')
        return self.get_clipboard_content()

    def get_clipboard_content(self):
        """Returns what is currently copied in the system clipboard."""
        with OperatingSystem._tk() as clipboard_content:
            return clipboard_content

    def pause(self):
        """Shows a dialog that must be dismissed with manually clicking.

        This is mainly for when you are developing the test case and want to
        stop the test execution.

        It should probably not be used otherwise.
        """
        ag.alert(text='Test execution paused.', title='Pause',
                 button='Continue')

    def terminate_application(self, alias=None):
        """Terminates the process launched with `Launch Application` with
        given ``alias``.

        If no ``alias`` is given, terminates the last process that was
        launched.
        """
        if alias and alias not in self.defaults.open_applications:
            raise InvalidAlias(alias)
        process = self.defaults.open_applications.pop(alias, None)
        if not process:
            try:
                _, process = self.defaults.open_applications.popitem()
            except KeyError as e:
                raise OSException('`Terminate Application` called without '
                                  '`Launch Application` called first.') from e
        process.terminate()

    def launch_application(self, appandargs:list, alias=None):
        """Launches an application.

        Executes the string argument ``app`` as a separate process with
        Python's
        ``[https://docs.python.org/2/library/subprocess.html|subprocess]``
        module. It should therefore be the exact command you would use to
        launch the application from command line.

        On Windows, if you are using relative or absolute paths in ``app``,
        enclose the command with double quotes:

        | Launch Application | "C:\\my folder\\myprogram.exe" | # Needs quotes       ||||
        | Launch Application | myprogram.exe | # No need for quotes ||||
        | Launch Application | myprogram.exe | arg1 | arg2 | # Program with arguments ||
        | Launch Application | myprogram.exe | alias=myprog | # Program with alias |||
        | Launch Application | myprogram.exe | arg1 | arg2 | alias=myprog | # Program with arguments and alias |

        Returns automatically generated alias which can be used with `Terminate
        Application`.

        Automatically generated alias can be overridden by providing ``alias``
        yourself.
        """
        if not alias:
            alias = str(len(self.defaults.open_applications))
        process = subprocess.Popen(args=appandargs)
        self.defaults.open_applications[alias] = process
        return alias

    def get_pid_of_launched_app(self, alias):
        """
        TODO Doc
        """
        if alias not in self.defaults.open_applications:
            raise InvalidAlias(alias)
        return self.defaults.open_applications[alias].pid

    def get_all_launched_apps(self):
        """
        TODO Doc
        """
        return_list = {}
        for alias, process in self.defaults.open_applications.items():
            return_list[alias] = process.pid
        return return_list
