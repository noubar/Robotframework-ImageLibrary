    
from ..modules.interaction.screenshot import Screenshot
from robot.api.deco import keyword

class ScreenshotKeywords():
    """
    TODO Doc
    """
    def __init__(self, screenshots):
        self.module = Screenshot(screenshots)

    @keyword
    def take_a_screenshot(self, allscreens=False):
        '''Takes a screenshot of the screen.

        This keyword is run on failure if it is not overwritten when
        `importing` the library.

        Screenshots are saved to the current working directory or in the
        ``screenshot_folder`` if such is defined during `importing`.

        The file name for the screenshot is the current suite name with a
        running integer appended. If this keyword is used outside of Robot
        Framework execution, file name is this library's name with running
        integer appended.
        '''
        self.module.take_a_screenshot(allscreens)
