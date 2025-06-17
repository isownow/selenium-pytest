@login
Feature: Login
    Testing scenarios for login feature

    Background:
        Given the user is on the login page

    @positive
    Scenario: Successful login
        When the user clicks login button by entering the valid credentials
        Then they should be redirected to the home page
        And the user's name should be visible on the homepage

    @negative
    Scenario Outline: Login with incorrect email
        When the user clicks login button after entering the valid password but incorrect email <email>
        Then an error message "Your email or password is incorrect!" should be displayed
        Examples:
            | email                |
            | johnsmith0@jon.com   |
            | johnsmith09@okay.com |
            | invalid.email@xyu    |

    @negative
    Scenario Outline: Login with incorrect password
        When the user clicks login button after entering the valid email but incorrect password <password>
        Then an error message "Your email or password is incorrect!" should be displayed
        Examples:
            | password   |
            | D0cker!Xy  |
            | 0cker!Xyz  |
            | Docker!Xyz |
            | 12345      |

    @negative
    Scenario Outline: Login with invalid email/password
        When the user clicks login button after entering the email <email> and password <password>
        Then an error message <expected_message> should be displayed for the <scenario> case with email <email> and password <password>
        Examples:
            | scenario               | email                 | password         | expected_message                                                             |
            | empty_email            | EMPTY                 | correct_password | Please fill out this field.                                                  |
            | empty_password         | correct_email         | EMPTY            | Please fill out this field.                                                  |
            | email_incomplete       | johnsmith09@          | correct          | Please enter a part following '@'. 'johnsmith09@' is incomplete.             |
            | email_without_@        | johnsmith09           | correct          | Please include an '@' in the email address. 'johnsmith09' is missing an '@'. |
            | email_domain_incorrect | jonsmith@okay@jon.com | correct          | A part following '@' should not contain the symbol '@'.                      |