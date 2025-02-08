*** Settings ***
Library     ${CURDIR}${/}..${/}..${/}..${/}src${/}ImageLibrary
...         ${CURDIR}${/}reference_images    screenshot_folder=${OUTPUT_DIR}    AS    Image
Library     OperatingSystem
Library     Process
Resource    ${PLATFORM_NAME}.robot


*** Variables ***
${EXP_WINDOW_TITLE}     FlaUI WPF Test App
${WRONG_PID}            99989
${TEST_APP_WPF}         ${CURDIR}${/}..${/}..${/}apps${/}WpfApplication
${TEST_APP_NOTIFIER}    ${CURDIR}${/}..${/}..${/}apps${/}Notifier
${TEST_APP_MFC}         ${CURDIR}${/}..${/}..${/}apps${/}MFCApplication
${TEST_APP_PAINT}       ${CURDIR}${/}..${/}..${/}apps${/}FormsPaint
${TEST_APP_KEYBOARD}    ${CURDIR}${/}..${/}..${/}apps${/}KeyboardTestConsole
${WPF_HANDLE}           None
${NOTIFIER_HANDLE}      None
${MFC_HANDLE}           None
${PAINT_HANDLE}         None
${KEYBOARD_HANDLE}      None


*** Keywords ***
Close Keyboard Test App
    Terminate Process    handle=${WPF_HANDLE}    kill=${True}
