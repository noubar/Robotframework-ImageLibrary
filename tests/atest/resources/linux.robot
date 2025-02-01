*** Settings ***
Library     Process
Library     OperatingSystem


*** Keywords ***
Process Should Be Running
    [Arguments]    ${name}
    ${_output}    OperatingSystem.Run    ps -C ${name}
    Should Contain    ${_output}    ${name}    msg=Process ${name} is not running

Process Should Not Be Running
    [Arguments]    ${name}
    ${_output}    OperatingSystem.Run    ps -C ${name}
    Should Not Contain    ${_output}    ${name}    msg=Process ${name} is running
