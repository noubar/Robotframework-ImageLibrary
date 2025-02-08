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

Open Keyboard Test App
    ${_status}    Run Keyword And Return Status    Process Should Be Running    name=KeyboardTestConsole
    IF    ${_status}    RETURN
    ${_handle}    Process.Start Process    ${TEST_APP_KEYBOARD}
    Set Global Variable    ${WPF_HANDLE}    ${_handle}
    Process Should Be Running    name=KeyboardTestConsole
