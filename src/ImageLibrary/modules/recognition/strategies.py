from skimage.feature import match_template, peak_local_max, canny
from skimage.color import rgb2gray
from skimage.io import imread, imsave
import pyautogui
import numpy as np
from robot.api import logger as LOGGER
from pyscreeze import ImageNotFoundException

class _StrategySkimage():
    _SKIMAGE_DEFAULT_CONFIDENCE = 0.99

    def __init__(self, recognitions):
        self.recognitions = recognitions

    def try_locate(self, ref_image, haystack_image=None, locate_all=False):
        """Tries to locate the reference image on the screen or the provided haystack_image. 
        Return values: 
        - locate_all=False: None or 1 location tuple (finds max 1)
        - locate_all=True:  None or list of location tuples (finds 0..n)
          (GUI Debugger mode)"""
        ih = self.recognitions
        confidence = ih.confidence or self._SKIMAGE_DEFAULT_CONFIDENCE        
        # with ih._suppress_keyword_on_failure():        
        needle_img = imread(ref_image, as_gray=True)
        needle_img_name = ref_image.split("\\")[-1].split(".")[0]
        # haystack_img_height, needle_img_width = needle_img.shape
        needle_img_height, needle_img_width = needle_img.shape
        if haystack_image is None:
            haystack_img_gray = rgb2gray(np.array(pyautogui.screenshot(allScreens=True)))
        else:
            haystack_img_gray = rgb2gray(haystack_image)

        # Canny edge detection on both images
        ih.needle_edge = self.detect_edges(needle_img)
        ih.haystack_edge = self.detect_edges(haystack_img_gray)  

        # peakmap is a "heatmap" of matching coordinates      
        ih.peakmap = match_template(ih.haystack_edge, ih.needle_edge, pad_input=True)

        # For debugging purposes
        debug = False
        if debug:
            imsave(needle_img_name + "needle.png", needle_img)
            imsave(needle_img_name + "needle_edge.png", ih.needle_edge)
            imsave(needle_img_name + "haystack.png", haystack_img_gray)
            imsave(needle_img_name + "haystack_edge.png", ih.haystack_edge)
            imsave(needle_img_name + "peakmap.png", ih.peakmap)

        if locate_all: 
            # https://stackoverflow.com/questions/48732991/search-for-all-templates-using-scikit-image                
            peaks = peak_local_max(ih.peakmap,threshold_rel=confidence) 
            peak_coords = zip(peaks[:,1], peaks[:,0])
            location = []
            for i, pk in enumerate(peak_coords):
                x = pk[0]
                y = pk[1]    
                # higest peak level
                peak = ih.peakmap[y][x]        
                if peak > confidence:                                       
                    loc = (x-needle_img_width/2, y-needle_img_height/2,
                           needle_img_width, needle_img_height)                    
                    location.append(loc)

        else:
            # translate highest index in peakmap from linear (memory) into 
            # an index of a matrix with the peakmaps dimensions
            ij = np.unravel_index(np.argmax(ih.peakmap), ih.peakmap.shape)
            # Extract coordinates of the highest peak; xy is the coordinate
            # where the CENTER of the reference image matched.
            x, y = ij[::-1]
            # higest peak level
            peak = ih.peakmap[y][x]   
            if peak > confidence:                       
                # tuple of xy (topleft) and width/height         
                location = (x-needle_img_width/2, y-needle_img_height/2,
                            needle_img_width, needle_img_height)
            else:
                location = None
        # TODO: Also return peak level
        return location

    def _detect_edges(self, img, sigma, low, high):
        edge_img = canny(
            image=img,
            sigma=sigma,
            low_threshold=low,
            high_threshold=high,
        )
        return edge_img

    def detect_edges(self, img):
        """Apply edge detection on a given image"""
        return self._detect_edges(
            img,
            self.ih_instance.edge_sigma,
            self.ih_instance.edge_low_threshold,
            self.ih_instance.edge_low_threshold
            )

class _StrategyPyautogui():
    def __init__(self, recognitions):
        self.confidence = float(recognitions.confidence)

    def try_locate(self, ref_image, haystack_image=None, locate_all=False):
        """Tries to locate the reference image on the screen or the haystack_image. 
        Return values: 
        - locate_all=False: None or 1 location tuple (finds max 1)
        - locate_all=True:  None or list of location tuples (finds 0..n)
          (GUI Debugger mode)"""
        location = None
        if haystack_image is None:
            haystack_image = pyautogui.screenshot(allScreens=True)
        if locate_all:
            locate_func = pyautogui.locateAll
        else:
            locate_func = pyautogui.locate  #Copy below,take screenshots
        # with ih._suppress_keyword_on_failure():
        try:
            if self.confidence:
                location_res = locate_func(ref_image,
                                           haystack_image,
                                           confidence=self.confidence)
            else:
                # if self.confidence:
                    # LOGGER.warn(" you don't "
                    #             "have OpenCV (opencv-python) installed "
                    #             "or a confidence level was not given.")
                location_res = locate_func(ref_image, haystack_image)
        except ImageNotFoundException as ex:
            LOGGER.info(ex)
            pass
        if locate_all:
            # convert the generator fo Box objects to a list of tuples
            location = [tuple(box) for box in location_res]
        else:
            # Single Box
            location = location_res
        return location
