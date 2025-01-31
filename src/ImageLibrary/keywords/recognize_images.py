import pyautogui as ag
from robot.api import logger as LOGGER
from robot.api.deco import keyword
from ..modules.interaction.os import OperatingSystem
from ..modules.recognition.images import RecognizeImage
from ..modules.errors import ImageNotOnScreenException

class RecognizeImagesKeywords(object):

    def __init__(self,defaults, platform, recognitions):
        self.recognitions = recognitions
        self.copy = OperatingSystem(defaults, platform).copy
        self.recognizer = RecognizeImage(defaults, self.recognitions)

    @keyword
    def click_image(self, reference_image, additional_timeoute=0):
        """Finds the reference image on screen and clicks it's center point once.

        ``reference_image`` is automatically normalized as described in the
        `Reference image names`.

        ``additional_timeoute`` optional value added to default timeout, in whole seconds. 
            default is 0
        """
        timeout = self.recognitions.timeout + additional_timeoute
        center_location = self.recognizer.wait_for(reference_image, timeout)
        LOGGER.info(f'Clicking image "{reference_image}" in position {center_location}')
        ag.click(center_location)
        return center_location

    def _click_to_the_direction_of(self, direction, location, offset, 
                                   clicks, button, interval):
        raise NotImplementedError('This is defined in the main class.')

    def _locate_and_click_direction(self, direction, reference_image, offset,
                                    clicks, button, interval, timeout):
        location = self.recognizer.wait_for(reference_image, timeout)
        self._click_to_the_direction_of(direction, location, offset, clicks,
                                        button, interval)

    @keyword
    def click_to_the_above_of_image(self, reference_image, offset, clicks=1,
                                    button='left', interval=0.0, additional_timeoute=0):
        """Clicks above of reference image by given offset.

        See `Reference image names` for documentation for ``reference_image``.

        ``offset`` is the number of pixels from the center of the reference
        image.

        ``clicks`` and ``button`` are documented in `Click To The Above Of`.

        ``timeout`` optional value, in whole seconds. default is 0
        """
        timeout = self.recognitions.timeout + additional_timeoute
        self._locate_and_click_direction('up', reference_image, offset,
                                         clicks, button, interval, timeout)

    @keyword
    def click_to_the_below_of_image(self, reference_image, offset, clicks=1,
                                    button='left', interval=0.0, additional_timeoute=0):
        """Clicks below of reference image by given offset.

        See argument documentation in `Click To The Above Of Image`.
        """
        timeout = self.recognitions.timeout + additional_timeoute
        self._locate_and_click_direction('down', reference_image, offset,
                                         clicks, button, interval, timeout)

    @keyword
    def click_to_the_left_of_image(self, reference_image, offset, clicks=1,
                                   button='left', interval=0.0, additional_timeoute=0):
        """Clicks left of reference image by given offset.

        See argument documentation in `Click To The Above Of Image`.
        """
        timeout = self.recognitions.timeout + additional_timeoute
        self._locate_and_click_direction('left', reference_image, offset,
                                         clicks, button, interval, timeout)

    @keyword
    def click_to_the_right_of_image(self, reference_image, offset, clicks=1,
                                    button='left', interval=0.0, additional_timeoute=0):
        """Clicks right of reference image by given offset.

        See argument documentation in `Click To The Above Of Image`.
        """
        timeout = self.recognitions.timeout + additional_timeoute
        self._locate_and_click_direction('right', reference_image, offset,
                                         clicks, button, interval, timeout)

    @keyword
    def copy_from_the_above_of(self, reference_image, offset, additional_timeoute=0):
        """Clicks three times above of reference image by given offset and
        copies.

        See `Reference image names` for documentation for ``reference_image``.

        See `Click To The Above Of Image` for documentation for ``offset``.

        Copy is done by pressing ``Ctrl+C`` on Windows and Linux and ``⌘+C``
        on OS X.

        ``timeout`` optional value, in whole seconds. default is 0
        """
        timeout = self.recognitions.timeout + additional_timeoute
        self._locate_and_click_direction('up', reference_image, offset,
                                         clicks=3, button='left', interval=0.0, timeout=timeout)
        return self.copy()

    @keyword
    def copy_from_the_below_of(self, reference_image, offset, additional_timeoute=0):
        """Clicks three times below of reference image by given offset and
        copies.

        See argument documentation in `Copy From The Above Of`.
        """
        timeout = self.recognitions.timeout + additional_timeoute
        self._locate_and_click_direction('down', reference_image, offset,
                                         clicks=3, button='left', interval=0.0, timeout=timeout)
        return self.copy()

    @keyword
    def copy_from_the_left_of(self, reference_image, offset, additional_timeoute=0):
        """Clicks three times left of reference image by given offset and
        copies.

        See argument documentation in `Copy From The Above Of`.
        """
        timeout = self.recognitions.timeout + additional_timeoute
        self._locate_and_click_direction('left', reference_image, offset,
                                         clicks=3, button='left', interval=0.0, timeout=timeout)
        return self.copy()

    @keyword
    def copy_from_the_right_of(self, reference_image, offset, additional_timeoute=0):
        """Clicks three times right of reference image by given offset and
        copies.

        See argument documentation in `Copy From The Above Of`.
        """
        timeout = self.recognitions.timeout + additional_timeoute
        self._locate_and_click_direction('right', reference_image, offset,
                                         clicks=3, button='left', interval=0.0, timeout=timeout)
        return self.copy()

    @keyword
    def does_exist(self, reference_image):
        """Returns ``True`` if reference image was found on screen or
        ``False`` otherwise. Never fails.

        See `Reference image names` for documentation for ``reference_image``.
        """
        # with self._suppress_keyword_on_failure():
        try:
            return bool(self.recognizer.locate(reference_image, log_it=True))
        except ImageNotOnScreenException:
            return False

    @keyword
    def locate(self, reference_image):
        """Locate image on screen.

        Fails if image is not found on screen.

        Returns Python tuple ``(x, y)`` of the coordinates matching the center point of the reference image.
        """
        return self.recognizer.locate(reference_image)

    @keyword
    def wait_for(self, reference_image, timeout=10):
        """Tries to locate given image from the screen for given time.

        Fail if the image is not found on the screen after ``timeout`` has
        expired.

        See `Reference images` for further documentation.

        ``timeout`` is given in whole seconds.

        Returns Python tuple ``(x, y)`` of the coordinates matching
        the center point of the reference image.
        """
        self.recognizer.wait_for(reference_image, timeout)

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
