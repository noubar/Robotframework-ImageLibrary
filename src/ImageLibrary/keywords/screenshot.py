from ..modules.interaction.screenshot import Screenshot
from robot.api.deco import keyword
from .inputhandle.commoninput import CommonInput
from .inputhandle.inputerrors import ScreenshotInputException

class ScreenshotKeywords():
    """
    TODO Doc
    """
    def __init__(self, screenshots):
        self.module = Screenshot(screenshots)

    @keyword
    def take_screenshot(self, allscreens=False):
        '''Takes a screenshot of the screen.

        Screenshots are saved to the current working directory or in the
        ``screenshot_folder`` if such is defined during `importing`.

        The file name for the screenshot is the current suite name with a
        running integer appended. If this keyword is used outside of Robot
        Framework execution, the file name is this library's name with a running
        integer appended.
        '''
        self.module.take_screenshot(CommonInput.validate_bool(allscreens,
                                                        ScreenshotInputException.AllScreensValue))
