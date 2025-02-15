class ImageLibraryError(ImportError):
    pass

class LibraryImportError(ImportError):
    pass

class ImageNotOnScreenException(Exception):

    @staticmethod
    def NotOnScreen(x):
        return ImageNotOnScreenException(f'Reference image "{x}" was not found on screen')

    @staticmethod
    def NotOnScreenAfterWait(x,y):
        return ImageNotOnScreenException(f'Reference image "{x}" was not found on screen '
                                         f'after waiting for the given timeout of "{y}" seconds.')

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

class InvalidAlias(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return (f'The given alias"{self.value}" is invalid '
                'or not launched yet using this library.')
