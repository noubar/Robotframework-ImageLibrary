*** Settings ***
Resource    resources/common.robot
# Suite Setup    Launch application    python    ${CURDIR}${/}keyboard${/}keyboard.py    alias=keyboard
# Suite Teardown    Terminate application
# Suite Setup    Launch App    ${TEST_APP_KEYBOARD}    alias=keyboardConsole
# Suite Teardown    Terminate Process    alias=keyboardConsole


*** Test Cases ***
Test
    click above of    1    12, 12    clicks=s
