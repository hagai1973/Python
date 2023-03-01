*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library           SeleniumLibrary

*** Variables ***
${LOGIN URL}      https://automationplayground.com/crm/
${BROWSER}        Chrome

*** Test Cases ***
Valid Login
    [tags]  Regression
    Open Browser To Login Page
     [Teardown]    Close Browser

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${LOGIN URL}    ${BROWSER}
#    Title Should Be    Login Page
