*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library           SeleniumLibrary
*** Variables ***
${LOGIN URL}      https://automationplayground.com/crm/
${BROWSER}        Chrome
${USER_NAME}       HAGAI


*** Test Cases ***
Valid Login
    [tags]  Regression
    Open Browser To Login Page
    Close Browser


Invalid Login
    [Documentation]         going to test invalid login
    [tags]  Regression      Sanity
    Open Browser To Login Page
    Check Page title
    sleep           3s
    Go sign in
    sleep           5s


*** Keywords ***
Open Browser To Login Page
    Open Browser    ${LOGIN URL}    ${BROWSER}
#    Title Should Be    Login Page


Check Page title
    Title Should Be   Customer Service


Go sign in
    click element               xpath=//*[@id="SignIn"]