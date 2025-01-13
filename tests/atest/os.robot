*** Settings ***
Documentation       Test suite for operating system keywords.
...

Resource            resources/common.robot
Library             StringFormat


*** Test Cases ***
Test Launch And Terminate
    Launch Application    ${TEST_APP_WPF}
    Sleep    3
    Process Should Be Running    WpfApplication
    Terminate Application
    Process Should Not Be Running    WpfApplication

Test Get Pid
    Launch Application    ${TEST_APP_WPF}    alias=alias1
    ${pid}    Get Pid Of All Launched Apps
    ${status}    Evaluate    len(${pid}.items()) == 1
    Should Be True    ${status}
    ${pid}    Get Pid Of Launched App    alias1
    ${status}    Evaluate    '${pid}'.isnumeric()
    Should Be True    ${status}
    Launch Application    ${TEST_APP_WPF}    alias=alias2
    ${pid}    Get Pid Of All Launched Apps
    ${status}    Evaluate    len(${pid}.items()) == 2
    Should Be True    ${status}
    ${pid}    Get Pid Of Launched App    alias1
    ${status}    Evaluate    '${pid}'.isnumeric()
    Should Be True    ${status}
    Terminate Application    alias1
    ${pid}    Get Pid Of All Launched Apps
    ${status}    Evaluate    len(${pid}.items()) == 1
    Should Be True    ${status}
    Terminate Application    alias2
