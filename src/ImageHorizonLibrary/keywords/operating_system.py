from ..modules.interaction.operating_system import OperatingSystem
from robot.api.deco import keyword
from robot.api import logger as LOGGER

class OperatingSystemKeywords(object):
    """
    TODO Doc
    """
    def __init__(self, defaults, platform):
        self.module = OperatingSystem(defaults, platform)

    @keyword
    def launch_application(self, *appandargs, alias=None):
        """Launches an application.

        Executes the string argument ``app`` as a separate process with
        Python's
        ``[https://docs.python.org/3/library/subprocess.html|subprocess]``
        module. It should therefore be the exact command you would use to
        launch the application from command line.

        On Windows, if you are using relative or absolute paths in ``app``,
        enclose the command with double quotes:

        | Launch Application | "C:\\my folder\\myprogram.exe" | # Needs quotes |
        | Launch Application | myprogram.exe | # No need for quotes |
        | Launch Application | myprogram.exe | arg1 | arg2 | # Program with arguments |
        | Launch Application | myprogram.exe | alias=myprog | # Program with alias |
        | Launch Application | myprogram.exe | arg1 | arg2 | alias=myprog | # Program with arguments and alias |

        Automatic generated alias is an index number.
        it can be overridden by providing ``alias`` yourself.

        This keyword returns the set alias which can be used with `Terminate
        Application` keyword.

        """
        self.module.launch_application(list(appandargs), alias=alias)

    @keyword
    def terminate_application(self, alias=None):
        """Terminates the process launched with `Launch Application` with
        given ``alias``.

        If no ``alias`` is given, terminates the last process that was
        launched.
        """
        self.module.terminate_application(alias)

    @keyword
    def get_pid_of_launched_app(self, alias):
        """
        TODO Doc
        """
        return self.module.get_pid_of_launched_app(alias)

    @keyword
    def get_pid_of_all_launched_apps(self):
        """
        TODO Doc
        """
        return self.module.get_all_launched_apps()

    @keyword
    def copy(self):
        """
        TODO Doc
        """
        self.module.copy()
