# -*- coding: utf-8 -*-
import shlex
import subprocess

from ..modules.errors import OSException


class OperatingSystemKeywords(object):
    """
    TODO Doc
    """
    def __init__(self, orchesterer):
        self.orchesterer = orchesterer

    def launch_application(self, app, alias=None):
        '''Launches an application.

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
        '''
        if not alias:
            alias = str(len(self.orchesterer.open_applications))
        process = subprocess.Popen(shlex.split(app))
        self.orchesterer.open_applications[alias] = process
        return alias

    def terminate_application(self, alias=None):
        '''Terminates the process launched with `Launch Application` with
        given ``alias``.

        If no ``alias`` is given, terminates the last process that was
        launched.
        '''
        if alias and alias not in self.orchesterer.open_applications:
            raise OSException(f'Invalid alias "{alias}".')
        process = self.orchesterer.open_applications.pop(alias, None)
        if not process:
            try:
                _, process = self.orchesterer.open_applications.popitem()
            except KeyError as e:
                raise OSException('`Terminate Application` called without '
                                  '`Launch Application` called first.') from e
        process.terminate()
