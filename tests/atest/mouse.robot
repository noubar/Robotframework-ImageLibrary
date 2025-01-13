*** Settings ***
Resource    resources/common.robot


*** Test Cases ***
Test Click
    # Launch Application    ${TEST_APP_PAINT}
    # Sleep    3
    Click To    60    60
    &{a}    Create Dictionary    x=400    y=400
    Click To    ${a}
    @{a}    Create List    500    500
    Click To    ${a}
    Move To    100    100

Test Drag And Drop
    # Launch Application    ${TEST_APP_PAINT}
    # Sleep    3
    &{a}    Create Dictionary    x=100    y=100
    &{b}    Create Dictionary    x=200    y=200
    Drag And Drop To    ${a}    ${b}    duration=2
    Drag And Drop To    200    200    300    100    duration=2
    @{a}    Create List    300    100
    @{b}    Create List    100    100
    Drag And Drop To    ${a}    ${b}    duration=2
