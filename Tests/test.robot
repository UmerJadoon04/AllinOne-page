*** Settings ***
Library    SeleniumLibrary
Library    Collections
Library    OperatingSystem

*** Variables ***
${URL}             https://rahulshettyacademy.com/AutomationPractice/#/
${NAME}            Umer Jadoon
${EXPECTED_PRICE}  296

*** Test Cases ***
Example Test Case
    Open Browser    ${URL}    chrome
    Select Radio Button
    Enter Autocomplete Text
    Select From Autocomplete
    Select Dropdown Option
    Check Checkbox
    Handle Windows
    Handle Tabs
    Fill Form And Verify Alert
    Verify Course List
    Calculate And Verify Sum
    Perform Mouse Hover
    Close Browser

*** Keywords ***
Select Radio Button
    Wait Until Element Is Visible    xpath=//input[@value='radio2']    timeout=10
    Click Element    xpath=//input[@value='radio2']

Enter Autocomplete Text
    Input Text    id=autocomplete    Pa

Select From Autocomplete
    ${elements}=    Get WebElements    class_name=ui-menu-item
    FOR    ${course}    IN    @{elements}
        ${text}=    Get Text    ${course}
        Run Keyword If    '${text}'=='Pakistan'    Click Element    ${course}
        Break
    END

Select Dropdown Option
    Select From List By Value    id=dropdown-class-example    option3

Check Checkbox
    Click Element    id=checkBoxOption1

Handle Windows
    ${current_window}=    Get Window Handle
    Click Element    id=openwindow
    ${all_windows}=    Get Window Handles
    ${new_window}=    Evaluate    [window for window in ${all_windows} if window != '${current_window}'][0]
    Switch Window    ${new_window}
    Wait Until Element Is Visible    link_text=Courses    timeout=10
    Click Link    link_text=Courses
    Close Window
    Switch Window    ${current_window}

Handle Tabs
    ${current_tab}=    Get Window Handle
    Click Element    id=opentab
    ${all_tabs}=    Get Window Handles
    ${new_tab}=    Evaluate    [tab for tab in ${all_tabs} if tab != '${current_tab}'][0]
    Switch Window    ${new_tab}
    Wait Until Element Is Visible    link_text=Courses    timeout=10
    Click Link    link_text=Courses
    Close Window
    Switch Window    ${current_tab}

Fill Form And Verify Alert
    Input Text    id=name    ${NAME}
    Click Element    id=alertbtn
    ${alert_text}=    Get Alert Text
    Should Contain    ${alert_text}    ${NAME}
    Accept Alert

Verify Course List
    ${courses}=    Get WebElements    xpath=(//body/div[3]/div[1]/fieldset[1]/table[1])//tr/td[2]
    ${browser_list}=    Create List
    FOR    ${course}    IN    @{courses}
        ${text}=    Get Text    ${course}
        Append To List    ${browser_list}    ${text}
    END
    ${new_course_list}=    Copy List    ${browser_list}
    Should Be Equal As Lists    ${new_course_list}    ${browser_list}

Calculate And Verify Sum
    Click Element    id=show-textbox
    Input Text    id=displayed-text    Show text
    ${prices}=    Get WebElements    xpath=(//body/div[3]/div[2]/fieldset[2]/div[1])//tr/td[4]
    ${sum}=    Evaluate    sum([int(price.text) for price in ${prices}])
    Should Be Equal As Numbers    ${sum}    ${EXPECTED_PRICE}

Perform Mouse Hover
    Move Mouse To    id=mousehover
    Move Mouse To    link_text=Top

Close Browser
    Close All Browsers

















