Feature: Selection from dropdown

    Scenario: Select multiple options from a dropdown
        Given I open the website "https://demo.mobiscroll.com/select/multiple-select"
        When I select "Books" and "Health & Beauty" from the dropdown
        Then both options "Books" and "Health & Beauty" should be selected