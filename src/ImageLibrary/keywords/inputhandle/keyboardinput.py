import pyautogui
from .inputerrors import KeyboardInputException

class KeyboardInput:
    """
    A utility class for validating and processing keyboard input for keyboard keywords.
    """

    @staticmethod
    def is_valid_key(key: str) -> str:
        """
        Checks if the given key is a valid keyboard key and returns it in lowercase.

        Args:
            key (str): The key to validate.

        Returns:
            str: The valid key in lowercase.

        Raises:
            KeyboardInputException: If the key is not a recognized keyboard key.
        """
        key = str(key).lower()
        if key in pyautogui.KEYBOARD_KEYS:
            return key
        raise KeyboardInputException(key)

    @staticmethod
    def validate_keys(keys: list) -> list:
        """
        Validates a list of keyboard keys.

        Args:
            keys (list): A list of keys to validate.

        Returns:
            list: A list of valid keys in lowercase.

        Raises:
            KeyboardInputException: If any key in the list is invalid.
        """
        return [KeyboardInput.is_valid_key(key) for key in keys]

    @staticmethod
    def validate_keys_or_text(keys: list) -> list:
        """
        Validates a list of keyboard keys and/or text inputs.

        This function processes a mix of raw text and key identifiers (e.g., 'key.enter').
        It extracts valid keyboard keys while preserving non-key text values.

        Args:
            keys (list): A list containing keyboard keys and/or text.

        Returns:
            list: A list where valid keys are normalized and as given as list item ['key'], 
            and non-key text remains unchanged.
        """
        validated_keys = []
        for key in keys:
            key_lower = key.lower()
            if key_lower.startswith('key.'):
                key = key_lower.split('key.')[1]
                key = KeyboardInput.is_valid_key(key)
                validated_keys.append([key])
            else:
                validated_keys.append(key)
        return validated_keys
