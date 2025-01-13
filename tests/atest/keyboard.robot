*** Settings ***
Resource    resources/common.robot
# Suite Setup    Launch application    python    ${CURDIR}${/}keyboard${/}keyboard.py    alias=keyboard
# Suite Teardown    Terminate application
Library     FlaUILibrary


*** Test Cases ***
Test
    No Operation
    Launch Application
