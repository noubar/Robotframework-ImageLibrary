from robot.api import logger as LOGGER
from robot.api.deco import keyword
from .inputhandle.recognitioninput import RecognitionInput
from .inputhandle.commoninput import CommonInput
from .inputhandle.inputerrors import OSInputException,RecognitionInputException

class OrganizeKeywords:
    """
    TODO Doc
    """
    def __init__(self,defaults, platform, recognitions, screenshots):
        self.defaults = defaults
        self.platform = platform
        self.recognitions = recognitions
        self.screenshots = screenshots

    @keyword
    def set_keyword_on_failure(self, keyword_on_failure):
        """Sets keyword to be run, when image library fails.

        This keyword might be used to temporarily diable screenshots, 
        then re-enable them later in the test.
        This keyword does not check if the keyword exists.

        See `library importing` for he usage of keyword_on_failure.
        """
        self.defaults.keyword_on_failure = keyword_on_failure

    @keyword
    def set_recognition_strategy(self, strategy):
        """Sets the strategy used for image recognition.
        available strategies are 'pyautogui'='default' and 'skimage'='edge'.
        """
        self.recognitions.strategy = RecognitionInput.validate_strategy(strategy)

    @keyword
    def set_edge_strategy_values(self, strategy):
        """Sets the strategy used for image recognition.
        available strategies are 'pyautogui'='default' and 'skimage'='edge'.
        """
        self.recognitions.strategy = RecognitionInput.validate_strategy(strategy)

    @keyword
    def set_reference_folder(self, edge_sigma=2.0, edge_low_threshold=0.1,
                         edge_high_threshold=0.3,):
        """Sets sigma low and high thresholds values needed by skimage.
        Confidence can be set using `Set Confidence` keyword, which is used by 
        both edge and default strategies.

        See `library importing` for format of the reference folder path.
        """
        self.recognitions.edge_sigma =  CommonInput.validate_float(
                                            edge_sigma, RecognitionInputException.EdgeSigma )
        self.recognitions.edge_low_threshold =  CommonInput.validate_float_between(
                                            edge_low_threshold, 0, 1, RecognitionInputException.LowThreshold )
        self.recognitions.edge_high_threshold =  CommonInput.validate_float_between(
                                            edge_high_threshold, 0, 1, RecognitionInputException.HighThreshold )

    @keyword
    def set_screenshot_folder(self, screenshot_folder_path):
        """Sets the folder where screenshots are saved to.

        See `library importing` for more specific information.
        """
        self.defaults.screenshot_folder = CommonInput.validate_path_exist(
            screenshot_folder_path, OSInputException.ScreenshotPath)

    @keyword
    def reset_confidence(self):
        """Resets the confidence level to the library default.
        If no confidence was given during import, then this equals to None.
        """
        self.recognitions.confidence = self.recognitions.initial_confidence
        LOGGER.info(f'Resetting confidence level to {self.recognitions.initial_confidence}.')

    @keyword
    def set_confidence(self, new_confidence):
        """Sets the accuracy when finding images.

        ``new_confidence`` is a decimal number between 0 and 1 inclusive.

        See `Confidence level` about additional dependencies that needs to be
        installed before this keyword has any effect.
        """
        self.recognitions.confidence = CommonInput.validate_float_between(
                                            new_confidence,0,1,RecognitionInputException.ConfidenceValue)
        LOGGER.info(f'Confidence level set to {self.recognitions.confidence}.')
