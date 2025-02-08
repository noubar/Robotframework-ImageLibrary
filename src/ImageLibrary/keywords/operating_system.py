from ..modules.interaction.os import OperatingSystem
from robot.api.deco import keyword
from robot.api import logger as LOGGER
import os

class OperatingSystemKeywords(object):
    """
    TODO Doc
    """
    def __init__(self, defaults, platform):
        self.module = OperatingSystem(defaults, platform)

    @keyword
    def start_subprocess(self, *appandargs, alias=None):
        """starts a process.

        Executes the string argument ``app`` as a separate process with
        Python's
        ``[https://docs.python.org/3/library/subprocess.html|subprocess]``
        module. It should therefore be the exact command you would use to
        launch the application from command line.

        On Windows, if you are using relative or absolute paths in ``app``,
        enclose the command with double quotes:

        | Start Subprocess | "C:\\my folder\\myprogram.exe" | # Needs quotes |
        | Start Subprocess | myprogram.exe | # No need for quotes |
        | Start Subprocess | myprogram.exe | arg1 | arg2 | # Program with arguments |
        | Start Subprocess | myprogram.exe | alias=myprog | # Program with alias |
        | Start Subprocess | myprogram.exe | arg1 | arg2 | alias=myprog | # Program with arguments and alias |

        Automatic generated alias is an index number.
        it can be overridden by providing ``alias`` yourself.

        This keyword returns the set alias which can be used with `Terminate
        Application` keyword.

        """
        self.module.subprocess(list(appandargs), alias=alias)

    @keyword
    def launch_app(self, path, *args, name=None, alias=None, timeout=10):
        """starts a process. 

        Executes the string argument ``app`` as a separate process with
        Python's
        ``[https://docs.python.org/3/library/subprocess.html|subprocess]``
        module. It should therefore be the exact command you would use to
        launch the application from command line.

        First arg should be the path of the app wanted to be lunched.
        enclose the command with double quotes:

        | Launch App | "C:\\my folder\\myprogram.exe" | # Needs quotes       |
        | Launch App | myprogram.exe | name=myprogram.exe | # No need for quotes |
        | Launch App | myprogram.exe | arg1 | arg2 | name=myprogram.exe | # Program with arguments |
        | Launch App | myprogram.exe | alias=myprog | name=myprogram.exe | # Program with alias |
        | Launch App | myprogram.exe | arg1 | arg2 | name=myprogram.exe | alias=myprog | # Program with arguments and alias |

        Automatic generated alias is an index number.
        it can be overridden by providing ``alias`` yourself.

        This keyword returns the set alias which can be used with `Terminate
        Application` keyword.

        """
        name = name if name else os.path.basename(path)
        path = os.path.abspath(path)
        if not os.path.exists(path):
            raise FileNotFoundError(f"The specified path does not exist: {path}")
        self.module.launch_app(path, args, process_name=name, alias=alias, timeout=timeout)

    @keyword
    def terminate_subprocess(self, alias=None, kill=False):
        """Terminates the process launched with `Launch App` or `start subprocess` with
        given ``alias`` or the last one.

        If no ``alias`` is given, terminates the last process that was
        launched.
        """
        self.module.terminate_subprocess(alias, kill)

    @keyword
    def kill_app(self, alias=None):
        """Terminates the process launched with `Launch App` or `start subprocess` with
        given ``alias`` or the last one.
        difference from `terminate subprocess` makes sure that process is not running anymore
        it tryes to terminate if not kill if not then force kill 

        If no ``alias`` is given, terminates the last process that was
        launched.
        """
        self.module.terminate_subprocess(alias)

    @keyword
    def get_pid_of_subprocess(self, alias):
        """
        Takes the alias and returns the process id of thesubprocess or launched application.
        The app should be launched with `Launch Application` keyword.
        """
        return self.module.get_pid_of_subprocess(alias)

    @keyword
    def get_pid_of_all_subprocesses(self):
        """
        Returns the process id of all the subprocesses and launched applications.
        """
        return self.module.get_all_subprocesses()

    @keyword
    def copy(self):
        """
        Presses ctrl/command + c to copy.
        """
        self.module.copy()

    @keyword
    def paste(self):
        """
        Presses ctrl/command + v to paste.
        """
        self.module.paste()

    @keyword
    def get_platform_name(self):
        """
        returns one of [windows,linux,mac] according your os
        """
        return self.module.platform.name

    @keyword
    def pause_popup(self):
        """
        Shows a dialog that must be dismissed with manually clicking.

        This is mainly for when you are developing the test case and want to
        stop the test execution.

        It should probably not be used otherwise.
        """
        self.module.pause()

    @keyword
    def normalize_path(self, relpath, validate=False):
        """
        Takes relative path and return an abstract full path.
        if validate is true checks also if the path isfile or isdir and its exists
        """
        self.module.abspath(relpath, validate)
