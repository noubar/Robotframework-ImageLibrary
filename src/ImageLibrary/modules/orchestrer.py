from collections import OrderedDict
from platform import platform
from os.path import isdir
from subprocess import call
import pyautogui
from .errors import ReferenceFolderException, StrategyException
from .recognition.strategies import _StrategyPyautogui, _StrategySkimage


class Orchesterer:
    """
    TODO Doc
    """
    def __init__(self):
        pass

    class Defaults:
        """
        TODO Doc
        """
        def __init__(self, reference_folder, keyword_on_failure):
            self.set_reference_folder(reference_folder)
            self.keyword_on_failure = keyword_on_failure
            self.open_applications = OrderedDict()

        def set_reference_folder(self, reference_folder):
            """
            Check if reference folder is valid.
            """
            if (not reference_folder or
                    not isinstance(reference_folder, str)):
                raise ReferenceFolderException('Reference folder is invalid: '
                                            f'"{reference_folder}"')
            if not isdir(reference_folder):
                raise ReferenceFolderException('Reference folder does not exist: '
                                           f'"{reference_folder}"')
            self.reference_folder = reference_folder

    class Platform:
        """
        TODO Doc
        """
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

            def platform_name(self):
                """Returns name of current platform: windows, mac, linux, or None"""
                name = None
                if self.is_linux():
                    name = 'linux'
                elif self.is_windows():
                    name = 'windows'
                elif self.is_mac():
                    name = 'mac'
                return name

        def __init__(self):
            utils = self.Utils()
            self.is_windows = utils.is_windows()
            self.is_mac = utils.is_mac()
            self.is_linux = utils.is_linux()
            self.has_retina = utils.has_retina()
            self.name = utils.platform_name()

    class Recognitions:
        """
        TODO Doc
        """

        def __init__(self, confidence, strategy, edge_sigma, edge_low_threshold,
                     edge_high_threshold, timeout):
            self.initial_confidence = confidence
            self.timeout = timeout
            self.needle_edge = None
            self.haystack_edge = None
            self.peakmap = None
            self.pixel_ratio = None
            self.set_strategy(strategy, edge_sigma, edge_low_threshold,
                              edge_high_threshold, confidence)
            self.set_pixel_ratio()

        def set_pixel_ratio(self):
            """ Sets the pixel ratio for the current screen. """
            self.pixel_ratio = pyautogui.screenshot().size[0]/pyautogui.size().width

        def set_strategy(self, strategy, edge_sigma=2.0, edge_low_threshold=0.1,
                         edge_high_threshold=0.3, confidence=0.99):
            """Changes the way how images are detected on the screen. 
            This can also be done globally during `Importing`.
            Strategies:
            - ``default`` - image recognition with pyautogui
            - ``edge`` - Advanced image recognition options with canny edge detection

            The ``edge`` strategy allows these additional parameters:
                - ``edge_sigma`` - Gaussian blur intensity
                - ``edge_low_threshold`` - low pixel gradient threshold
                - ``edge_high_threshold`` - high pixel gradient threshold

            Both strategies can optionally be initialized with a new confidence."""

            self.strategy = strategy
            self.confidence = confidence
            if strategy == 'default':
                self.strategy = _StrategyPyautogui(self)
            elif strategy == 'edge':
                self.edge_sigma = edge_sigma
                self.edge_low_threshold = edge_low_threshold
                self.edge_high_threshold = edge_high_threshold
                self.strategy = _StrategySkimage(self)
            else:
                raise StrategyException(strategy)
            # Linking protectelocate to the strategy's method
            self.try_locate = self.strategy.try_locate

    class Screenshots:
        """
        TODO Doc
        """

        def __init__(self, folder, name=""):
            self.folder = folder
            self.counter = 1
            self.set_name(name)

        def set_name(self, name):
            """
            Set screenshot filename as lower text.
            Removes all invalid windows syntax and replace all empty characters into '_'

            Args:
                name (str): Filename to set.
            """
            self.name = self._clean_invalid_windows_syntax(name.replace(" ", "_").lower())

        @staticmethod
        def _clean_invalid_windows_syntax(filename, special_characters="\"|%:/,.\\[]<>*?"):
            return ''.join([c for c in filename if c not in special_characters])

