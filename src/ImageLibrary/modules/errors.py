class ExceptionBuilder:
    def __init__(self, exception: type[Exception], message: str, *args):
        formatted_message = message.format(*args)
        raise exception(formatted_message)
    
class ImageLibraryError(ImportError):
    pass

class LibraryImportError(ImportError):
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

class InvalidAlias(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return (f'The given alias"{self.value}" is invalid '
                'or not launched yet using this library.')
