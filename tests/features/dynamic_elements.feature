@dynamic_elements
Feature: Dynamic Element Handling Across Multiple Websites

    # 1. Explicit Wait + Alert Handling
    @dynamic_alert
    Scenario: Handle dynamic alert after form submission on TestAutomationCentral
        Given I open the website "https://testautomationcentral.com/demo/stepper_forms.html"
        When I fill in the form with valid data
        And I click the Submit button
        Then I should see a dynamic alert with the message "Form submitted successfully!"

    # 2. Explicit Wait + Element Visibility
    @element_visibility
    Scenario: Wait for hidden element to appear on The-Internet
        Given I open the website "https://the-internet.herokuapp.com/dynamic_loading/1"
        When I click the Start button
        Then I should wait until the "Hello World!" text is visible

    # 3. Dynamic enablement
    @element_enable
    Scenario: Wait for dynamically enabled button on DemoQA
        Given I open the website "https://demoqa.com/dynamic-properties"
        When I wait for the first button to become enabled
        Then I should be able to click the button without error

    # 4. Dynamic Color Change
    @dynamic_color_change
    Scenario: Detect text color change on DemoQA button
        Given I open the website "https://demoqa.com/dynamic-properties"
        When I wait for the button to change its text color
        Then the button's text color is changed to red "rgba(220, 53, 69, 1)"

# # 5. Stale Element Handling
# Scenario: Handle stale element after DOM update on The-Internet
#     Given I open the website "https://the-internet.herokuapp.com/dynamic_controls"
#     When I click the Remove button
#     Then I should wait until the checkbox disappears
#     And I should not get a stale element exception

# # 6. Dynamic Table Interaction
# Scenario: Extract data from a dynamic table on Guru99
#     Given I open the website "https://demo.guru99.com/test/web-table-element.php"
#     When I fetch the number of rows and columns
#     Then I should print the company names and current prices

# # 7. Overlay or Modal Handling
# Scenario: Handle modal popup overlay on DemoQA
#     Given I open the website "https://demoqa.com/modal-dialogs"
#     When I click the Show Small Modal button
#     Then I should wait for the modal to appear
#     And I should close the modal successfully

# # 8. Iframe with Dynamic Content
# Scenario: Switch to iframe and interact with dynamic content
#     Given I open the website "https://demoqa.com/frames"
#     When I switch to the first iframe
#     Then I should verify the heading inside the iframe