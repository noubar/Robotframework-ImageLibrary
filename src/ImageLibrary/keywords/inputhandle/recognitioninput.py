import os
from enum import Enum
from .inputerrors import RecognitionInputException

class Strategy(Enum):
    """
    Represents available image recognition strategies.
    """
    default = 'default'
    pyautogui = 'default'
    edge = 'edge'
    skimage = 'edge'

class RecognitionInput:
    """
    A utility class for validating and processing image recognition inputs.
    """
    def __init__(self, defaults, recognitions):
        self.defaults = defaults
        self.recognitions = recognitions

    @staticmethod
    def validate_strategy(name: str) -> str:
        """
        Validates the given image recognition strategy name.

        Args:
            name (str): The name of the image recognition strategy.
            Valid strategies are ('default' or 'pyautogui', 'edge' or 'skimage').
        """
        name = name.lower()
        if name in ['default', 'pyautogui', 'edge', 'skimage']:
            return Strategy[name].value
        else:
            raise RecognitionInputException.StrategyValue(name)

    def validate_additional_timeout(self, seconds: int,) -> int:
        """
        Validates the given image recognition strategy name.

        Args:
            seconds (int): added timoute to the default timeout.
        """
        try:
            seconds = int(seconds) + self.recognitions.timeout
        except ValueError as e:
            raise RecognitionInputException.Timeout(seconds) from e
        if seconds < 0:
            raise RecognitionInputException.Timeout(seconds)
        return seconds

    def validate_image_ref(self, name: str, exception) -> str:
        """
        Validates the given image path according to the given reference name.
        image path can be a file or a folder. in case of folder returns all images in the folder.

        Args:
            name (str): the file name of an image under the reference folder.
            or a folder name under the reference folder.

            exception (Exception): the exception to raise if the image 
            is not found under reference folder or the directory is not found under reference folder.
        """
        ref = []
        name = str(name.lower().replace(' ', '_'))
        path = os.path.abspath(os.path.join(self.defaults.reference_folder, name))
        isdir = os.path.isdir(path)
        if isdir:
            for f in os.listdir(path):
                image = os.path.join(path, f)
                if not os.path.isfile(image):
                    raise exception(path)
                ref.append(image)
        else:
            if not path.endswith('.png'):
                path += '.png'
            if not os.path.isfile(path):
                raise exception(path)
            ref = path
        return ref

    def validate_single_image_ref(self, name: str, exception) -> str:
        """
        Validates the given image path according to the given reference name.

        Args:
            name (str): the file name of an image under the reference folder.

            exception (Exception): the exception to raise if the image 
            is not found under reference folder.    
        """
        name = str(name.lower().replace(' ', '_'))
        path = os.path.abspath(os.path.join(self.defaults.reference_folder, name))
        if not path.endswith('.png'):
            path += '.png'
        if not os.path.isfile(path):
            raise exception(path)
        return path
