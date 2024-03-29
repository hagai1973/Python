imarily used by higher-level keywords like Input Username.

*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library           SeleniumLibrary

*** Variables ***
${LOGIN URL}      https://automationplayground.com/crm/
${BROWSER}        Chrome

#robot -d .\Results\  -N "Web Demo tests"   ./Tests/Web/Web_Demo.robot

*** Test Cases ***
Valid Login
    Open Browser To Login Page
#    Input Username    demo
#    Input Password    mode
#    Submit Credentials
#    Welcome Page Should Be Open
#    [Teardown]    Close Browser

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Title Should Be    Customer Service

Input Username
    [Arguments]    ${username}
    Input Text    username_field    ${username}

Input Password
    [Arguments]    ${password}
    Input Text    password_field    ${password}

Submit Credentials
    Click Button    login_button

Welcome Page Should Be Open
    Title Should Be    Welcome Page