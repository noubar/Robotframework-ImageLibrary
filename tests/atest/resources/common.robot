*** Settings ***
Library     ${CURDIR}${/}..${/}..${/}..${/}src${/}ImageLibrary
...         ${CURDIR}${/}reference_images    screenshot_folder=${OUTPUT_DIR}    AS    Image
Library     OperatingSystem
Library     Process


*** Variables ***
${EXP_WINDOW_TITLE}     FlaUI WPF Test App
${WRONG_PID}            99989
${TEST_APP_WPF}         ${CURDIR}${/}..${/}..${/}apps${/}WpfApplication
${TEST_APP_NOTIFIER}    ${CURDIR}${/}..${/}..${/}apps${/}Notifier
${TEST_APP_MFC}         ${CURDIR}${/}..${/}..${/}apps${/}MFCApplication
${TEST_APP_PAINT}       ${CURDIR}${/}..${/}..${/}apps${/}FormsPaint


*** Keywords ***
Process Should Be Running
    [Arguments]    ${name}
    ${_output}    OperatingSystem.Run    powershell.exe "Get-Process -Name ${name} | Format-List -Property ProcessName"
    Should Contain    ${_output}    ProcessName : ${name}    msg=Process ${name} is not running

Process Should Not Be Running
    [Arguments]    ${name}
    ${_output}    OperatingSystem.Run    powershell.exe "Get-Process -Name ${name} | Format-List -Property ProcessName"
    Should Not Contain    ${_output}    ProcessName : ${name}    msg=Process ${name} is running
