# -*- coding: utf-8 -*-
from platform import platform
from subprocess import call

class Utils():
    """
    A class containing utility functions for checking the current platform and
    determining if it has a retina display.
    """

    def __init__(self):
        self.platform = platform()

    def is_windows(self):
        """
        Checks if the current platform is Windows.
        :return: True if the platform is Windows, False otherwise.
        """
        return self.platform.lower().startswith('windows')


    def is_mac(self):
        """
        Checks if the current platform is macOS.
        :return: True if the platform is macOS, False otherwise.
        """
        return self.platform.lower().startswith('darwin')


    def is_linux(self):
        """
        Checks if the current platform is linux.
        :return: True if the platform is linux, False otherwise.
        """
        return self.platform.lower().startswith('linux')


    def is_java(self):
        """
        Checks if the current platform is java.
        """
        return self.platform.lower().startswith('java')

    def has_retina(self):
        """
        Checks if the current platform has a retina display.
        :return: True if the platform has a retina display, False otherwise.
        """
        if self.is_mac():
            # Will return 0 if there is a retina display
            return call("system_profiler SPDisplaysDataType | grep 'Retina'", shell=True) == 0
        return False

