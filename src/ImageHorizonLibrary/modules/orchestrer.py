from collections import OrderedDict
from .utils import Utils
from .errors import 
# import inspect
from .errors import ReferenceFolderException, StrategyException
from os.path import isdir
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
    class Platform:
        """
        TODO Doc
        """
        def __init__(self):
            utils = Utils()
            self.is_windows = utils.is_windows()
            self.is_mac = utils.is_mac()
            self.is_linux = utils.is_linux()
            self.has_retina = utils.has_retina()

    class Recognitions:
        """
        TODO Doc
        """

        def __init__(self, confidence, strategy, edge_sigma, edge_low_threshold, edge_high_threshold, timeout):
            self.initial_confidence = confidence
            self.timeout = timeout
            self.set_strategy(strategy, edge_sigma, edge_low_threshold, edge_high_threshold, confidence)


        def set_strategy(self, strategy, edge_sigma=2.0, edge_low_threshold=0.1, edge_high_threshold=0.3, confidence=None):
            """Changes the way how images are detected on the screen. This can also be done globally during `Importing`.
            Strategies:
            - ``default``
            - ``edge`` - Advanced image recognition options with canny edge detection

            The ``edge`` strategy allows these additional parameters:
                - ``edge_sigma`` - Gaussian blur intensity
                - ``edge_low_threshold`` - low pixel gradient threshold
                - ``edge_high_threshold`` - high pixel gradient threshold

            Both strategies can optionally be initialized with a new confidence."""

            self.strategy = strategy
            if strategy == 'default':
                self.strategy = _StrategyPyautogui(self)
            elif strategy == 'edge': 
                self.strategy = _StrategySkimage(self)
                self.edge_sigma = edge_sigma
                self.edge_low_threshold = edge_low_threshold
                self.edge_high_threshold = edge_high_threshold
            else: 
                raise StrategyException(strategy)
                
            if not confidence is None:
                self.set_confidence(confidence)

            # Linking protected _try_locate to the strategy's method
            self._try_locate = self.strategy._try_locate


    class Screenshots:
        """
        TODO Doc
        """

        def __init__(self, folder, counter=1, name=""):
            self.folder = folder
            self.counter = counter
            self._name = name

        def set_name(self, name):
            """
            Set screenshot filename as lower text.
            Removes all invalid windows syntax and replace all empty characters into '_'

            Args:
                name (str): Filename to set.
            """
            self._name = self._clean_invalid_windows_syntax(name.replace(" ", "_").lower())

        @staticmethod
        def _clean_invalid_windows_syntax(filename, special_characters="\"|%:/,.\\[]<>*?"):
            return ''.join([c for c in filename if c not in special_characters])
