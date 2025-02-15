import pyautogui as ag
from robot.api import logger as LOGGER
from robot.api.deco import keyword
from ..modules.recognition.images import RecognizeImage
from ..modules.errors import ImageNotOnScreenException
from .inputhandle.recognitioninput import RecognitionInput
from .inputhandle.commoninput import CommonInput
from .inputhandle.inputerrors import RecognitionInputException

class RecognizeImagesKeywords(object):

    def __init__(self,defaults, recognitions):
        self.recognitions = recognitions
        self.defaults = defaults
        self.recognizer = RecognizeImage(defaults, recognitions)
        self.module = self.recognizer
        self.recin = RecognitionInput(defaults, recognitions)

    @keyword
    def locate(self, reference_image):
        """Locate image on screen.
        it gets image center
        Fails if image is not found on screen.

        Returns Python tuple ``(x, y)`` of the coordinates matching 
        the center point of the reference image.
        """
        return self.module.locate(self.recin.validate_single_image_ref(reference_image, RecognitionInputException.ImageRef))

    @keyword
    def wait_for(self, reference_image, timeout=10):
        """Tries to locate given image from the screen for given time.
        image name should exist under reference folder, png file extestion is added automatically.

        Fail if the image is not found on the screen after ``timeout`` has
        expired.
        
        See `Reference images` for further documentation.

        ``timeout`` is independent of the default timeout and given in seconds.

        Returns Python tuple ``(x, y)`` of the coordinates matching
        the center point of the reference image.
        Which can be used in other keywords and be saved as robot variable.
        """
        self.module.wait_for(self.recin.validate_single_image_ref(reference_image, RecognitionInputException.ImageRef),
                            CommonInput.validate_float(timeout, RecognitionInputException.Timeout))

    @keyword
    def click_image(self, reference_image, additional_timeout=0):
        """Finds the reference image on screen and clicks its center point once.

        ``reference_image`` is automatically normalized as described in the
        `Reference image names`.

        ``additional_timeout`` optional value added to the default timeout, in whole seconds.
        The additional timeout could also be negative, which would decrease the default timeout.
        in this case the default timeout should be set to a value greater than additional_timeout.
            default timeout is 0 and can be set by library initiation (library import).

        """
        self.module.click_image(self.recin.validate_single_image_ref(reference_image, RecognitionInputException.ImageRef),
                                self.recin.validate_additional_timeout(additional_timeout))

    @keyword
    def click_above_of_image(self, reference_image, offset, clicks=1,
                                    button='left', interval=0.0, additional_timeout=0):
        """Clicks above the reference image by given offset.

        See `Reference image names` for documentation for ``reference_image``.

        ``offset`` is the number of pixels from the center of the reference
        image.

        ``clicks`` and ``button`` are documented in `Click To The Above Of`.

        ``timeout`` optional value, in whole seconds. default is 0
        """
        self.module.locate_and_click_direction('up', 
                self.recin.validate_single_image_ref(reference_image, RecognitionInputException.ImageRef),
                offset,
                clicks,
                button,
                interval,
                self.recin.validate_additional_timeout(additional_timeout))

    @keyword
    def click_below_of_image(self, reference_image, offset, clicks=1,
                                    button='left', interval=0.0, additional_timeout=0):
        """Clicks below the reference image by given offset.

        See argument documentation in `Click To The Above Of Image`.
        """
        timeout = self.recognitions.timeout + additional_timeout
        self.module.locate_and_click_direction('down', reference_image, offset,
                                         clicks, button, interval, timeout)

    @keyword
    def click_left_of_image(self, reference_image, offset, clicks=1,
                                   button='left', interval=0.0, additional_timeout=0):
        """Clicks left of the reference image by given offset.

        See argument documentation in `Click To The Above Of Image`.
        """
        timeout = self.recognitions.timeout + additional_timeout
        self.module.locate_and_click_direction('left', reference_image, offset,
                                         clicks, button, interval, timeout)

    @keyword
    def click_right_of_image(self, reference_image, offset, clicks=1,
                                    button='left', interval=0.0, additional_timeout=0):
        """Clicks right of the reference image by given offset.

        See argument documentation in `Click To The Above Of Image`.
        """
        timeout = self.recognitions.timeout + additional_timeout
        self.module.locate_and_click_direction('right', reference_image, offset,
                                         clicks, button, interval, timeout)

    @keyword
    def does_exist(self, reference_image):
        """Returns ``True`` if reference image was found on screen or
        ``False`` otherwise. Never fails.

        See `Reference image names` for documentation for ``reference_image``.
        """
        # with self._suppress_keyword_on_failure():
        try:
            return bool(self.module.locate(reference_image, log_it=True))
        except ImageNotOnScreenException:
            return False

    @keyword
    def debug_image(self):
        """Halts the test execution and opens the image debugger UI.
        
        Whenever you encounter problems with the recognition accuracy of a reference image, 
        you should place this keyword just before the line in question. Example: 

        | Debug Image
        | Wait For  hard_to_find_button

        The test will halt at this position and open the debugger UI. Use it as follows:

        - Select the reference image (`hard_to_find_button`)
        - Click the button "Detect reference image" for the strategy you want to test (default/edge).
        The GUI hides itself while it takes the screenshot of the current application. 
        - The Image Viewer at the botton shows the screenshot with all regions where the reference image was found. 
        - "Matches Found": More than one match means that either `conficence` is set too low or that the 
        reference image is visible multiple times. If the latter is the case, you should first detect a unique 
        UI element and use relative keywords like `Click To The Right Of`.
        - "Max peak value" (only `edge`) gives feedback about the detection accuracy of the best match
          and is measured as a float number between 0 and 1. A peak value above _confidence_ results in a match. 
        - "Edge detection debugger" (only `edge`) opens another window where both the reference and screenshot
          images are shown before and after the edge detection and is very helpful to learn 
          how the sigma and low/high threshold parameters lead to different results. 
        - The field "Keyword to use this strategy" shows how to set the strategy to the current settings. 
        Just copy the line and paste it into the test: 

        | Set Strategy  edge  edge_sigma=2.0  edge_low_threshold=0.1  edge_high_threshold=0.3
        | Wait For  hard_to_find_button
        
        The purpose of this keyword is *solely for debugging purposes*; don't 
        use it in production!"""
        from ..modules.recognition.ImageDebugger import ImageDebugger
        debug_app = ImageDebugger(self)


"""
ToDo
- Add more keywords for image recognition
    Should Exist On Screen
    Should Not Exist On Screen
    Get Image Rectangle
    Get Image Size
    Get Image Width
    Get Image Height
    Get Image Center == 
"""