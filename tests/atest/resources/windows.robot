*** Settings ***
Library     Process
Library     OperatingSystem


*** Keywords ***
Process Should Be Running
    [Arguments]    ${name}
    ${_output}    OperatingSystem.Run    powershell.exe "Get-Process -Name ${name} | Format-List -Property ProcessName"
    Should Contain    ${_output}    ProcessName : ${name}    msg=Process ${name} is not running

Process Should Not Be Running
    [Arguments]    ${name}
    ${_output}    OperatingSystem.Run    powershell.exe "Get-Process -Name ${name} | Format-List -Property ProcessName"
    Should Not Contain    ${_output}    ProcessName : ${name}    msg=Process ${name} is running
