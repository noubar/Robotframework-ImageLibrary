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
