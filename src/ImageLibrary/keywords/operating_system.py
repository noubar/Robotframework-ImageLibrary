from ..modules.interaction.os import OperatingSystem
from robot.api.deco import keyword
from robot.api import logger as LOGGER

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
    def launch_app(self, *appandargs, name=None, alias=None, timeout=10):
        """starts a process. 

        Executes the string argument ``app`` as a separate process with
        Python's
        ``[https://docs.python.org/3/library/subprocess.html|subprocess]``
        module. It should therefore be the exact command you would use to
        launch the application from command line.

        On Windows, if you are using relative or absolute paths in ``app``,
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
        name = name if name else appandargs[0]
        self.module.launch_app(list(appandargs), name, alias=alias, timeout=timeout)

    @keyword
    def terminate_subprocess(self, alias=None):
        """Terminates the process launched with `Launch Application` with
        given ``alias``.

        If no ``alias`` is given, terminates the last process that was
        launched.
        """
        self.module.terminate_process(alias)

    @keyword
    def get_pid_of_launched_app(self, alias):
        """
        Takes the alias and returns the process id of the launched application.
        The app should be launched with `Launch Application` keyword.
        """
        return self.module.get_pid_of_launched_app(alias)

    @keyword
    def get_pid_of_all_launched_apps(self):
        """
        Returns the process id of all the launched applications.
        """
        return self.module.get_all_launched_apps()

    @keyword
    def copy(self):
        """
        Presses ctrl/command+c to copy.
        """
        self.module.copy()

    @keyword
    def paste(self):
        """
        Presses ctrl/command+v to paste.
        """
        self.module.paste()
