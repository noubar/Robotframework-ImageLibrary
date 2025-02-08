*** Settings ***
Library     Process
Library     OperatingSystem


*** Variables ***
${EXP_WINDOW_TITLE}             FlaUI WPF Test App
${WRONG_PID}                    99989
${START_CMD_TEST_APP_WPF}       ${TEST_APP_WPF}


*** Keywords ***
Process Should Be Running
    [Arguments]    ${name}
    ${_output}    OperatingSystem.Run    ps -C ${name}
    Should Contain    ${_output}    ${name}    msg=Process ${name} is not running

Process Should Not Be Running
    [Arguments]    ${name}
    ${_output}    OperatingSystem.Run    ps -C ${name}
    Should Not Contain    ${_output}    ${name}    msg=Process ${name} is running
