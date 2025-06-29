Feature: Core Concepts

    # find_elements + explicit wait
    Scenario: Using 'find_elements' to get all the boxes on the page
        Given I open the website "https://www.selenium.dev/selenium/web/dynamic.html"
        When I click the "Add a box!" button 10 times
        Then I wait for 10 boxes to appear on the page