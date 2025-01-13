# -*- coding: utf-8 -*-
class ImageLibraryError(ImportError):
    pass


class ImageNotOnScreenException(Exception):
    def __init__(self, image_name):
        self.image_name = image_name

    def __str__(self):
        return f'Reference image "{self.image_name}" was not found on screen'


class InvalidImageException(Exception):
    pass


class KeyboardException(Exception):
    pass


class MouseException(Exception):
    pass


class OSException(Exception):
    pass


class ReferenceFolderException(Exception):
    pass


class ScreenshotFolderException(Exception):
    pass

class StrategyException(Exception):
    def __init__(self, strategy):
        self.strategy = strategy

    def __str__(self):
        return (f'Invalid strategy: "{self.strategy}": '
        'it should be edge or default')

class InvalidConfidenceValue(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return (f'The given confidence value "{self.value}" is invalid: '
        'it should be a float number between 0 and 1')

class InvalidAlias(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return (f'The given alias"{self.value}" is invalid or not launched yet using this library.')
