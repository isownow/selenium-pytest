Feature: Perform user interactions using Selenium ActionChains

    # Check the actual visibilty of sub-menu (sub-menu is present in the DOM and can be located even if it is not visible to the user)
    @hover
    Scenario: Hover over a menu to reveal a submenu
        Given I open the website "https://demoqa.com/menu"
        When I hover over the "Main Item 2" menu
        Then I should see the submenu

    @right_click
    Scenario: Displaying alert on right-click context menu selection
        Given I open the website "https://swisnl.github.io/jQuery-contextMenu/demo.html"
        When I right-click on the context menu button
        And I select "delete" from the context menu
        Then I should see an alert with the message "clicked: delete"

    @double_click
    Scenario: Double-click a button to trigger a message
        Given I open the website "https://demoqa.com/buttons"
        When I double-click on the "Double Click Me" button
        Then I should see a confirmation message as "You have done a double click"

    @move_to_element
    Scenario: Hover over an element and click on a revealed link
        Given I open the website "https://the-internet.herokuapp.com/hovers"
        When I hover over the second avatar and click on the "View profile" link
        Then I should be navigated to the profile page

    @drag_and_drop
    Scenario: Drag and drop an element onto a target
        Given I open the website "https://selenium08.blogspot.com/2020/01/click-and-hold.html"
        When I move "C" to the position of item "A"
        Then the positions of item "C" and item "A" should be interchanged


# Scenario: Press keyboard keys with modifiers
#     Given I open the website "https://the-internet.herokuapp.com/key_presses"
#     When I press the SHIFT key and type "test"
#     Then the page should show the last key pressed

# Scenario: Release a held element
#     Given I open the website "https://demoqa.com/droppable"
#     When I click and hold the draggable box and release it on the drop area
#     Then the box should drop successfully