
*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library           SeleniumLibrary


*** Variables ***
${LOGIN URL}                https://automationplayground.com/crm/
${BROWSER}                  Chrome
${SIGN_IN_LINK} =            id=SignIn


*** Test Cases ***
Valid Login
    [Tags]      sample_test
    Open Browser To Login Page


*** Keywords ***
Open Browser To Login Page
    Open Browser        ${LOGIN URL}    ${BROWSER}
    click element       ${SIGN_IN_LINK}
    Title Should Be     Customer Service - Login


