
from time import time, sleep
from tkinter import Tk as TK
import os
import subprocess
import psutil
import pyautogui as ag
from .keyboard import Keyboard
from ..errors import OSException,InvalidAlias

class OperatingSystem:
    """
    TODO Doc
    """
    class _Clipboard:
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
        key = 'command' if self.platform.is_mac else 'ctrl'
        Keyboard.press_keys([key, 'c'])
        return self.get_clipboard_content()

    def paste(self):
        """Executes ``Ctrl+C`` on Windows and Linux, ``⌘+C`` on OS X and
        returns the content of the clipboard."""
        key = 'command' if self.platform.is_mac else 'ctrl'
        Keyboard.press_keys([key, 'v'])
        return True

    def get_clipboard_content(self):
        """Returns what is currently copied in the system clipboard."""
        with OperatingSystem._Clipboard() as clipboard_content:
            return clipboard_content

    def pause(self):
        """Shows a dialog that must be dismissed with manually clicking.

        This is mainly for when you are developing the test case and want to
        stop the test execution.

        It should probably not be used otherwise.
        """
        ag.alert(text='Test execution paused.', title='Pause',
                 button='Continue')

    def terminate_subprocess(self, alias=None, kill=False):
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
        if kill:
            process.kill()
        else:
            process.terminate()

    def launch_app(self, path, args:list, process_name, timeout=10, alias=None):
        """Launches an application. and awaits the process to start.
            It will not check if the process is already running.

        Process: The process name to be checked in the running processes.

        Executes the string argument ``app`` as a separate process with
        Python's
        ``[https://docs.python.org/2/library/subprocess.html|subprocess]``
        module. It should therefore be the exact command you would use to
        launch the application from command line.

        On Windows, if you are using relative or absolute paths in ``app``,
        enclose the command with double quotes:


        Returns automatically generated alias which can be used with `Terminate
        Application`.

        Automatically generated alias can be overridden by providing ``alias``
        yourself.
        """
        # Check if the path is absolute and enclose in double quotes if on Windows
        # On macOS, if it's an .app bundle, use `open`
        if not alias:
            alias = str(len(self.defaults.open_applications))
        if self.platform.is_mac and path.endswith(".app"):
           process = subprocess.Popen(["open", path, "--args"] + list(args))
        elif self.platform.is_windows:
            process = subprocess.Popen(["start", path] + list(args), shell=True)
        else:
            process = subprocess.Popen([path] + list(args))
        start_time = time()
        while time() - start_time < timeout:
            # Check all running processes
            for proc in psutil.process_iter(attrs=['name','status']):
                if proc.info['name'] == process_name and proc.info['status'] == 'running':
                    self.defaults.open_applications[alias] = process
                    return alias
            sleep(1)  # Wait before checking again
        self.defaults.open_applications.pop(alias, None)
        # If the process is not found, raise an exception
        raise OSException(f'Process "{process_name}" not found after {timeout} seconds.')

    def subprocess(self, appandargs:list, alias=None):
        """Launches an application.

        Executes the string argument ``app`` as a separate process with
        Python's
        ``[https://docs.python.org/2/library/subprocess.html|subprocess]``
        module. It should therefore be the exact command you would use to
        launch the application from command line.

        On Windows, if you are using relative or absolute paths in ``app``,
        enclose the command with double quotes:


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

    def get_pid_of_subprocess(self, alias=None):
        """
        TODO Doc
        pid of last subprocess or pid of subprocess with the given alias
        """
        if alias and alias not in self.defaults.open_applications:
            raise InvalidAlias(alias)
        else:
            alias = str(len(self.defaults.open_applications))
        return self.defaults.open_applications[alias].pid

    def get_all_subprocesses(self):
        """
        TODO Doc
        """
        return_list = {}
        for alias, process in self.defaults.open_applications.items():
            return_list[alias] = process.pid
        return return_list

    def abspath(self, relpath, validate:bool):
        """
        TODO Doc
        """
        path = os.path.abspath(relpath)
        if validate:
            if not os.path.isdir(path) and os.path.isfile(path):
                raise OSException()
            return path.abspath(relpath)
