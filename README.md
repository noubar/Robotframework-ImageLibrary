# ImageLibrary (Under Maintenance)

This Robot Framework library provides the facilities to automate GUIs based on
image recognition similar to Sikuli, but without any Java dependency (100% Python). 
Additionally, it supports other functionalities of pyautogui as Keywords.

**There are two different recognition strategies:**

- *default* (using [pyautogui](https://github.com/asweigart/pyautogui))
- *edge* (using [skimage](https://scikit-image.org/docs/dev/auto_examples/features_detection/plot_template.html)). 

For non pixel perfect matches, there is a feature called "confidence level" that 
allows to define the percentage of pixels which *must* match.

In the *default* strategy, confidence comes with a dependency to OpenCV (python package: `opencv-python`).

## Keyword documentation

[Keyword Documentation](./doc/ImageLibrary.html)


## Prerequisites

- `Python 3.x`
- [pip](https://pypi.python.org/pypi/pip) for easy installation
- [Robot Framework](http://robotframework.org)

On Ubuntu, you need to take [special measures](https://pyautogui.readthedocs.org/en/latest/screenshot.html#special-notes-about-ubuntu) to make the screenshot functionality to work correctly. The keyboard functions might not work on Ubuntu when run in VirtualBox on Windows.

### Development



## Installation

If you have pip, installation is straightforward:

``` pip install robotframework-imagelibrary ```

## Windows

ImageLibrary should work on Windows "out-of-the-box". Just run the commands above to install it.

## Linux
You additionally need to install these for pyautogui:

``` sudo apt-get install python-dev python-xlib ```

You might also need, depending on your Python distribution, to install:

``` sudo apt-get install python-tk ```

If you are using virtualenv, you must install python-xlib manually to the virtual environment for pyautogui:

Fetch the source distribution
Install with:

``` pip install python-xlib-<latest version>.tar.gz ```


## Mac

NOTICE Mac is **not maintained**, But open for contributions.

You may additionally need to install these for pyautogui:

``` pip install pyobjc-core pyobjc ```

For these, you need to install [XCode](https://developer.apple.com/xcode/downloads/)


## Running Unit Tests

``` python tests/utest/run_tests.py [verbosity=2] ```

## Running acceptance tests

``` python tests/atest/run_tests.py ```

Additionally to unit test dependencies, you also need OpenCV, Eel, scrot and Chrome/Chromium browser.
OpenCV is used because this tests are testing also confidence level.
Browser is used by Eel for cross-platform GUI demo application.
scrot is used for capturing screenshots.

``` pip install opencv-python eel ```

## Updating Docs

To regenerate documentation ([Keyword Documentation](./doc/ImageLibrary.html)), use this command:

```  python -m robot.libdoc -P ./src ImageLibrary doc/ImageLibrary.html ```
