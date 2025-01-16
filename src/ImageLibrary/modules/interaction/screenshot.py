from os.path import abspath, relpath, join as path_join
from robot.libraries.BuiltIn import BuiltIn, RobotNotRunningError
from robot.api import logger as LOGGER
import pyautogui as ag

from ..errors import ScreenshotFolderException

class Screenshot:

    def __init__(self, screenshots):
        self.screenshots = screenshots

    def _make_up_filename(self):
        try:
            path = f'{self.screenshots.name.replace(' ', '')}-screenshot'
        except RobotNotRunningError:
            LOGGER.info('Could not get suite name, using '
                        'default naming scheme')
            path = 'ImageHorizon-screenshot'
        path = f'{path}-{self.screenshots.counter}.png'
        self.screenshots.counter += 1
        return path

    def take_screenshot(self, allscreens: bool):
        '''Takes a screenshot of the screen.

        This keyword is run on failure if it is not overwritten when
        `importing` the library.

        Screenshots are saved to the current working directory or in the
        ``screenshot_folder`` if such is defined during `importing`.

        The file name for the screenshot is the current suite name with a
        running integer appended. If this keyword is used outside of Robot
        Framework execution, file name is this library's name with running
        integer appended.
        '''
        target_dir = self.screenshots.folder if self.screenshots.folder else ''
        if not isinstance(target_dir, str):
            raise ScreenshotFolderException('Screenshot folder is invalid: '
                                            f'"{target_dir}"' )
        path = self._make_up_filename()
        path = abspath(path_join(target_dir, path))
        # logpath = BuiltIn().get_variable_value('${OUTPUT DIR}')
        # relativepath = relpath(path, start=logpath).replace('\\', '\/')
        ag.screenshot(path, allScreens=allscreens)
        LOGGER.info('Screenshot taken: '
                    '{0}<br/><img src="{0}" width="100%" />'.format(path), html=True)
