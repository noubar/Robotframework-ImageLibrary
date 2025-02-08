*** Settings ***
Resource    resources/common.robot


*** Variables ***
&{dict_coordinates}         x=100    y=200
@{list_coordinates}         100    200
${string_coordinates}       100,200
${string_coordinates2}      100 ,200
${string_coordinates3}      100, 200
${string_coordinates4}      100 , 200


*** Test Cases ***
Test Clicking Using Different Coordinate Formats
    [Documentation]    Validate different ways of passing coordinates to the Click keyword.
    # Using a dictionary
    Click To    ${dict_coordinates}
    # Using a list
    Click To    ${list_coordinates}
    # Using a tuple
    ${tuple_coordinates}    Evaluate    (100, 200)
    Click To    ${tuple_coordinates}
    # Passing coordinates directly
    Click To    100    200
    # Using named arguments
    Click To    x=100    y=200
    # Passing coordinates as a comma-separated string
    Click To    ${string_coordinates}
    Click To    ${string_coordinates2}
    Click To    ${string_coordinates3}
    Click To    ${string_coordinates4}

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
