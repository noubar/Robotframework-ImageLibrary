from robot.api import logger as LOGGER
from robot.api.deco import keyword
from ..modules.errors import InvalidConfidenceValue

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
        """Sets keyword to be run, when location-related
        keywords fail.

        This keyword might be used to temporarily diable screenshots, 
        then re-enable them later in the test.

        See `library importing` for he usage of keyword_on_failure.
        """
        self.defaults.keyword_on_failure = keyword_on_failure

    @keyword
    def set_recognition_strategy(self, strategy):
        """Sets keyword to be run, when location-related
        keywords fail.

        This keyword might be used to temporarily diable screenshots, 
        then re-enable them later in the test.

        See `library importing` for he usage of keyword_on_failure.
        """
        self.recognitions.strategy = strategy

    @keyword
    def set_reference_folder(self, reference_folder_path):
        """Sets where all reference images are stored.

        See `library importing` for format of the reference folder path.
        """
        self.defaults.reference_folder = reference_folder_path

    @keyword
    def set_screenshot_folder(self, screenshot_folder_path):
        """Sets the folder where screenshots are saved to.

        See `library importing` for more specific information.
        """
        self.defaults.screenshot_folder = screenshot_folder_path

    @keyword
    def reset_confidence(self):
        """Resets the confidence level to the library default.
        If no confidence was given during import, then this equals to None."""
        LOGGER.info(f'Resetting confidence level to {self.recognitions.initial_confidence}.')
        self.recognitions.confidence = self.recognitions.initial_confidence
    @keyword
    def set_confidence(self, new_confidence):
        """Sets the accuracy when finding images.

        ``new_confidence`` is a decimal number between 0 and 1 inclusive.

        See `Confidence level` about additional dependencies that needs to be
        installed before this keyword has any effect.
        """
        if new_confidence is not None:
            try:
                new_confidence = float(new_confidence)
                if not 1 >= new_confidence >= 0:
                    LOGGER.warn(f'Unable to set confidence to {new_confidence}. Value '
                                'must be between 0 and 1, inclusive.')
                    raise(InvalidConfidenceValue(new_confidence))
                else:
                    self.recognitions.confidence = new_confidence
            except TypeError as e:
                LOGGER.warn(f"Can't set confidence to {new_confidence}")
                raise(InvalidConfidenceValue(new_confidence)) from e
        else:
            self.recognitions.confidence = None
