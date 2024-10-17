*** Settings ***
Library     ${CURDIR}${/}..${/}..${/}src${/}ImageHorizonLibrary
...             ${CURDIR}${/}reference_images${/}calculator    screenshot_folder=${OUTPUT_DIR}


*** Test Cases ***
Calculator
    Set Confidence    0.9
    Launch application    python    ${CURDIR}${/}calculator${/}calculator.py    alias=calc
    ${location1}=    Wait for    inputs_folder    timeout=30
    Click to the above of image    ${location1}    20
    Type    1010
    Click to the below of image    ${location1}    20
    Type    1001
    ${location2}=    Locate    or_button
    Click to the below of image    ${location2}    0
    Click to the below of image    ${location2}    50
    Sleep    0.1
    ${result}=    Copy
    Should be equal as integers    ${result}    1011
    Click Image    close_button
    [Teardown]    Terminate application

test
