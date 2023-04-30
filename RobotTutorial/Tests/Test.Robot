*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library           SeleniumLibrary


*** Variables ***
${LOGIN URL}      https://automationplayground.com/crm/
${BROWSER}        Chrome
${SIGN_IN_BUTTON} =   xpath=//a[@id="SignIn"]
${USERNAME_INPUT_LOCATOR} =         id=email-id
${PASSWORD_INPUT_LOCATOR} =         id=password
${USERNAME}                 Moshe@test.com
${PASSWORD}                 123456



*** Test Cases ***
Valid Login
    [Tags]    smoke
    Open Browser To Login Page
    type username       ${USERNAME}
    sleep           5s



*** Keywords ***
Open Browser To Login Page
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Title Should Be    Customer Service
    click element       ${SIGN_IN_BUTTON}
${PASSWORD_INPUT_LOCATOR}

type username${PASSWORD_INPUT_LOCATOR}
    [Arguments]    ${username}
    Input Text    ${USERNAME_INPUT_LOCATOR}     ${username}


type password
    [Arguments]    ${username}
    Input Text    ${PASSWORD_INPUT_LOCATOR}     ${username}
