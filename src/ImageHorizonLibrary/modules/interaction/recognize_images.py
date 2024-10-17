
from os.path import abspath, isdir, isfile, join as path_join
from os import listdir
from contextlib import contextmanager
from ..errors import InvalidImageException
import pyautogui as ag


class RecognizeImage():

    dflt_timeout = 0
    pixel_ratio = 0.0

    def __init__(self,defualts, recognizer):
        self.defualts = defualts
        self.recognizer = recognizer


    def _get_pixel_ratio(self):
        self.pixel_ratio = ag.screenshot().size[0]/ag.size().width

    def _normalize(self, path):
        if (not path or not isinstance(path, str)):
            raise InvalidImageException(f'"{path}" is invalid image name.' )
        path = str(path.lower().replace(' ', '_'))
        path = abspath(path_join(self.defualts.reference_folder, path))
        if not path.endswith('.png') and not isdir(path):
            path += '.png'
        if not isfile(path) and not isdir(path):
            raise InvalidImageException(f'Image path not found: "{path}".' )
        return path

    # @contextmanager
    # def _suppress_keyword_on_failure(self):
    #     keyword = self.defaults.keyword_on_failure
    #     self.defaults.keyword_on_failure = None
    #     yield None
    #     self.defaults.keyword_on_failure = keyword

    def _get_reference_images(self, reference_image):
        '''Return an absolute path for the given reference imge. 
        Return as a list of those if reference_image is a folder.
        '''
        is_dir = False
        try:
            if isdir(self._normalize(reference_image)):
                is_dir = True
        except InvalidImageException:
            pass
        is_file = False
        try:
            if isfile(self._normalize(reference_image)):
                is_file = True
        except InvalidImageException:
            pass
        reference_image = self._normalize(reference_image)

        reference_images = []
        if is_file:
            reference_images = [reference_image]
        elif is_dir:
            for f in listdir(self._normalize(reference_image)):
                if not isfile(self._normalize(path_join(reference_image, f))):
                    raise InvalidImageException(
                                            self._normalize(reference_image))
                reference_images.append(path_join(reference_image, f))
        return reference_images

    def _locate(self, reference_image, log_it=True):
        reference_images = self._get_reference_images(reference_image)

        location = None
        for ref_image in reference_images:
            location = self._try_locate(ref_image)
            if location != None:
                break

        if location is None:
            if log_it:
                LOGGER.info('Image "%s" was not found '
                            'on screen. (strategy: %s)' % (reference_image, self.strategy))
            self._run_on_failure()
            raise ImageNotFoundException(reference_image)

        center_point = ag.center(location)
        x = center_point.x
        y = center_point.y
        if self.pixel_ratio == 0.0:
            self.__get_pixel_ratio()
        if self.pixel_ratio>1:
            x = x / self.pixel_ratio
            y = y / self.pixel_ratio
        return (x, y)

    def _locate_all(self, reference_image, haystack_image=None):   
        '''Tries to locate all occurrences of the reference image on the screen
        or on the haystack image, if given.
        Returns a list of location tuples (finds 0..n)''' 
        reference_images = self._get_reference_images(reference_image)   
        if len(reference_images) > 1: 
            raise InvalidImageException(
                f'Locating ALL occurences of MANY files ({", ".join(reference_images)}) is not supported.')        
        locations = self._try_locate(reference_images[0], locate_all=True, haystack_image=haystack_image)
        return locations