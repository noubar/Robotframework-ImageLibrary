# -*- coding: utf-8 -*-
from contextlib import contextmanager
from robotlibcore import DynamicCore

from .modules.errors import *    # import errors before checking dependencies!

try:
    import pyautogui as ag
except ImportError as e:
    raise ImageLibraryError('There is something wrong with pyautogui or '
                                   'it is not installed.') from e
try:
    from robot.api import logger as LOGGER
    from robot.libraries.BuiltIn import BuiltIn
except ImportError as e:
    raise ImageLibraryError('There is something wrong with '
                                   'Robot Framework or it is not installed.') from e
try:
    from tkinter import Tk as TK
except ImportError as e:
    raise ImageLibraryError('There is either something wrong with '
                                   'Tkinter or you are running this on Java, '
                                   'which is not a supported platform. Please '
                                   'use Python and verify that Tkinter works.') from e
try:
    import skimage
except ImportError as e:
    raise ImageLibraryError('There is either something wrong with skimage '
                                    '(scikit-image) or it is not installed.') from e
try:
    import cv2
except ImportError as e:
    raise ImageLibraryError('There is either something wrong with cv2 '
                                    '(opencv-python) or it is not installed.') from e

from .keywords import(KeyboardKeywords,
                      ScreenshotKeywords,
                      OperatingSystemKeywords,
                      RecognizeImagesKeywords,
                      OrganizeKeywords,
                      MouseKeywords)

from .modules.utils import *
from .version import VERSION
from .modules.orchestrer import Orchesterer

__version__ = VERSION

class ImageLibrary(DynamicCore):
    """A cross-platform Robot Framework library for GUI automation.

    NOTE: To ensure x y coordinates are correct, the screen resolution scaling must be set to 100%.

    *Key features*: 
    - Automates *keyboard and mouse actions* on the screen 
    (based on [https://pyautogui.readthedocs.org|pyautogui]).
    - The regions to execute these actions on (buttons, sliders, input fields etc.) 
    are determined by `reference images` which the library detects on the screen -
    independently of the OS or the application type.
    - Two different image `recognition strategies`: `default` 
    (fast and reliable of predictable screen content),
    and `edge` (to facilitate the recognition of unpredictable pixel deviations)
    - The library can also take screenshots in case of failure or by intention.

    = Image Recognition = 

    == Reference images ==
    ``reference_image`` parameter can be either a single file or a folder.
    If ``reference_image`` is a folder, image recognition is tried separately
    for each image in that folder, in alphabetical order until a match is found.

    For ease of use, reference image names are automatically normalized
    according to the following rules:

    - The name is lower cased: ``MYPICTURE`` and ``mYPiCtUrE`` become
      ``mypicture``

    - All spaces are converted to underscore ``_``: ``my picture`` becomes
      ``my_picture``

    - If the image name does not end in ``.png``, it will be added:
      ``mypicture`` becomes ``mypicture.png``

    - Path to _reference folder_ is prepended. This option must be given when
      `importing` the library.

    Using good names for reference images is evident from easy-to-read test
    data:

    | `Import Library` | ImageLibrary                   | reference_folder=images |                                                            |
    | `Click Image`    | popup Window title                    |                         | # Path is images/popup_window_title.png                    |
    | `Click Image`    | button Login Without User Credentials |                         | # Path is images/button_login_without_user_credentials.png |

    == Recognition strategies ==
    Basically, image recognition works by searching a reference image on the 
    another image (a screnshot of the current desktop).
    If there is a region with 100% matching pixels of the reference image, this 
    area represents a match. 

    By default, the reference image must be an exakt sub-image of the screenshot.
    This works flawlessly in most cases. 
    
    But problems can arise when:

    - the application's GUI uses transpareny effects
    - the screen resolution/the window size changes
    - font aliasing is used for dynamic text
    - compression algorithms in RDP/Citrix cause invisible artifacts
    - ...and in many more situations.
    
    In those situations, a certain amount of the pixels do not match. 
    
    To solve this, ImageHorizon comes with a parameter ``confidence level``. This is a decimal value 
    between 0 and 1 (inclusive) and defines how many percent of the reference image pixels
    must match the found region's imag. It is set to 1.0 = 100% by default.

    Confidence level can be set during `library importing` and re-adjusted during the test 
    case with the keyword `Set Confidence`.
    
    === Default image detection strategy ===
    
    If imported without any strategy argument, the library uses 
    [https://pyautogui.readthedocs.org|pyautogui] 
    under the hood to recognize images on the screen. 
    This is the perfect choice to start writing tests. 

    To use `confidence level in mode` ``default`` the 
    [https://pypi.org/project/opencv-python|opencv-python] Python package
    must be installed separately:

    | $ pip install opencv-python

    After installation, the library will automatically use OpenCV for confidence 
    levels lower than 1.0.

    === The "edge" image detection strategy ===

    The default image recognition reaches its limitations when the area to 
    match contains a *disproportionate amount of unpredictable pixels*. 

    The idea for this strategy came from a problem in real life: a web application 
    showing a topographical map (loaded from a 3rd party provider), with a layer of 
    interstate highways as black lines. For some reasons, the pixels of topographic 
    areas between the highway lines (which are the vast majority) showed a slight
    deviation in brightness - invisible for the naked eye, but enough to make the test failing. 
    
    The abstract and simplified example for this is a horizontal black line of 1px width in a 
    matrix of 10x10 white pixels. To neglect a (slight) brightness deviation of the white pixels, 
    you would need a confidence level of 0.1 which allows 90% of the pixels to be 
    different. This is insanse and leads to inpredictable results. 
    
    That's why ``edge`` was implemented as an alternative recognition strategy.  
    The key here lies in the approach to *reduce both images* (reference and screenshot
    image) *to the essential characteristics* and then *compare _those_ images*. 

    "Essential characteristics" of an image are those areas where neighbouring pixels show a 
    sharp change of brightness, better known as "edges". 
    [https://en.wikipedia.org/wiki/Edge_detection|Edge detection] 
    is the process of finding the edges in an image, done by 
    [https://scikit-image.org/|scikit-image] in this library.
    
    As a brief digression, edge detection is a multi-step process:

    - apply a [https://en.wikipedia.org/wiki/Gaussian_filter|Gaussian filter] 
    (blurs the image to remove noise; intensity set by parameter `sigma`)
    - apply a [https://en.wikipedia.org/wiki/Sobel_operator|Sobel filter] 
    (remove non-max pixels, get a 1 pixel edge curve) 
    - separate weak edges from strong ones with 
    [https://en.wikipedia.org/wiki/Canny_edge_detector#Edge_tracking_by_hysteresis|hysteresis] 
    - apply the `template_matching` routine to get a 
    [https://en.wikipedia.org/wiki/Cross-correlation|cross correlation] 
    matrix of values from -1 (no correlation) to +1 (perfect correlation).
    - Filter out only those coordinates with values greater than the ``confidence`` level, 
    take the max

    The keyword `Debug Image` opens a debugger UI where confidence level, 
    Gaussian sigma and low/high thresholds can be tested and adjusted to individual needs.

    Edge detection costs some extra CPU time; you should always first try 
    to use the ``default`` strategy and only selectively switch to ``edge``
    when a confidence level below 0.9 is not sufficient to detect images reliably anymore: 

    | # use with defaults
    | Set Strategy  edge
    | # use with custom parameters
    | Set Strategy  edge  edge_sigma=2.0  edge_low_threshold=0.1  
    edge_high_threshold=0.3  confidence=0.8

    To use strategy ``edge``, the [https://scikit-image.org|scikit-image] 
    Python package must be installed separately:

    | $ pip install scikit-image

    = Performance =

    Locating images on screen, especially if screen resolution is large and
    reference image is also large, might take considerable time, regardless
    of the strategy.
    It is therefore advisable to save the returned coordinates if you are
    manipulating the same context many times in the row:

    | `Wait For`                   | label Name |     |
    | `Click To The Left Of Image` | label Name | 200 |

    In the above example, same image is located twice. Below is an example how
    we can leverage the returned location:

    | ${location}=           | `Wait For`  | label Name |
    | `Click To The Left Of` | ${location} | 200        |
    """    

    ROBOT_LIBRARY_SCOPE = 'Global'
    ROBOT_LIBRARY_VERSION = VERSION
    ROBOT_LISTENER_API_VERSION = 2

    def __init__(self, reference_folder=None, screenshot_folder=None,
                 keyword_on_failure='Take Screenshot',
                 confidence=0.99, strategy='default',
                 edge_sigma=2.0, edge_low_threshold=0.1, edge_high_threshold=0.3,
                 recognition_timeout=0):
        """ImageLibrary can be imported with several options.
        
        ``reference_folder`` is path to the folder where all reference images
        are stored. It must be a _valid absolute path_. As the library
        is suite-specific (ie. new instance is created for every suite),
        different suites can have different folders for it's reference images.

        ``screenshot_folder`` is path to the folder where screenshots are
        saved. If not given, screenshots are saved to the current working
        directory.

        ``keyword_on_failure`` is the keyword to be run, when location-related
        keywords fail. If you wish to not take screenshots, use for example
        `BuiltIn.No Operation`. Keyword must however be a valid keyword.
        
        ``strategy`` sets the way how images are detected on the screen. See also 
        keyword `Set Strategy` to change the strategy during the test. Parameters:
        - ``default`` - (Default)
        - ``edge`` - Advanced image recognition options with canny edge detection

        The ``edge`` strategy allows these additional parameters:
          - ``edge_sigma`` - Gaussian blur intensity
          - ``edge_low_threshold`` - low pixel gradient threshold
          - ``edge_high_threshold`` - high pixel gradient threshold

        ``recognition_timeout`` default timout in seconds for image recognition.
          
        """
        self.platform = Orchesterer.Platform()
        self.defaults = Orchesterer.Defaults(reference_folder, keyword_on_failure)
        self.screenshots = Orchesterer.Screenshots(screenshot_folder)
        self.recognitions = Orchesterer.Recognitions(confidence, strategy, edge_sigma,
                                                        edge_low_threshold, edge_high_threshold,
                                                        recognition_timeout)
        
        libraries = [KeyboardKeywords(),
                    MouseKeywords(),
                    ScreenshotKeywords(self.screenshots),
                    OperatingSystemKeywords(self.defaults, self.platform),
                    RecognizeImagesKeywords(self.defaults, self.platform, self.recognitions),
                    OrganizeKeywords(self.defaults, self.platform, self.recognitions, self.screenshots)
                    ]
        DynamicCore.__init__(self, libraries)

    def run_keyword(self, name, args, kwargs=None):
        try:
            return DynamicCore.run_keyword(self, name, args, kwargs)
        except Exception:
            if self.defaults.keyword_on_failure:
                self._run_on_failure()
            raise

    def _run_on_failure(self):
        if not self.defaults.keyword_on_failure:
            return
        try:
            BuiltIn().run_keyword(self.defaults.keyword_on_failure)
        except Exception as e:
            LOGGER.debug(e)
            LOGGER.warn('Failed to run keyword_on_failure in imagelibrary.'
                        'Is Robot Framework running')

    def _start_test(self, name, attrs):  # pylint: disable=unused-argument
        self.screenshots.set_name(name)
        self.screenshots.counter = 1
