from time import time
import pyautogui as ag
from robot.api import logger as LOGGER
from ..interaction.mouse import Mouse
from ..errors import InvalidImageException
from ..errors import ImageNotOnScreenException

class RecognizeImage():

    dflt_timeout = 0
    pixel_ratio = 0.0

    def __init__(self,defaults, recognitions):
        self.defaults = defaults
        self.recognitions = recognitions
        self.mouse = Mouse()

    def _get_pixel_ratio(self):
        self.pixel_ratio = ag.screenshot().size[0]/ag.size().width

    def locate(self, reference_image, log_it=True):
        """
        excpetcts valid reference image path and returns 
        the center point of the image on the screen.
        TODO Doc
        """
        location = self.recognitions.try_locate(reference_image)
        if not location:
            if log_it:
                LOGGER.info(f'Image "{reference_image}" was not found '
                            f'on screen. (strategy: {self.recognitions.strategy})')
            raise ImageNotOnScreenException.NotOnScreen(reference_image)
        center_point = ag.center(location)
        x = center_point.x
        y = center_point.y
        if self.pixel_ratio == 0.0:
            self._get_pixel_ratio()
        if self.pixel_ratio>1:
            x = x / self.pixel_ratio
            y = y / self.pixel_ratio
        return (x, y)

    def _locate_all(self, reference_images, haystack_image=None):
        """Tries to locate all occurrences of the reference image on the screen
        or on the haystack image, if given.
        Returns a list of location tuples (finds 0..n)"""
        if len(reference_images) > 1: 
            raise InvalidImageException(
                f'Locating ALL occurences of MANY files ({", ".join(reference_images)}) is not supported.')
        locations = self.recognitions.try_locate(reference_images[0], locate_all=True, haystack_image=haystack_image)
        return locations

    def wait_for(self, reference_image, timeout=10):
        """Tries to locate given image from the screen for given time.

        Fail if the image is not found on the screen after ``timeout`` has
        expired.

        See `Reference images` for further documentation.

        ``timeout`` is given in whole seconds.

        Returns Python tuple ``(x, y)`` of the coordinates matching
        the center point of the reference image.
        """
        stop_time = int(time()) + int(timeout)
        location = None
        # with self._suppress_keyword_on_failure():
        while int(time()) <= stop_time:
            try:
                location = self.locate(reference_image, log_it=True)
                break
            except ImageNotOnScreenException:
                pass
        if location is None:
            raise ImageNotOnScreenException.NotOnScreenAfterWait(reference_image,timeout)
        LOGGER.info(f'Image "{reference_image}" found at {location}')
        return location

    def click_image(self, reference_image, timeout):
        center_location = self.wait_for(reference_image, timeout)
        LOGGER.info(f'Clicking image "{reference_image}" in position {center_location}')
        ag.click(center_location)
        return center_location

    def locate_and_click_direction(self, direction, reference_image, offset,
                                    clicks, button, interval, timeout):
        location = self.wait_for(reference_image, timeout)
        self.mouse.click_to_direction_of(direction, offset, clicks,
                                        button, interval, location)
