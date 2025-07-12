@login
Feature: Login
    Testing scenarios for login feature

    Background:
        Given the user opens the website "https://automationexercise.com/"
        And the user goes to the login page

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

    # This test verifies session validity after loading cookies and performs a re-login if the server-side session is invalid or if the cookies are missing or expired on the client side.
    @positive @login_cookies
    Scenario: Reuse login session using cookies
        When the cookies are not available, I log in to get the cookies else I add the cookies
        And if the session is invalid, I login to get the cookies
        Then the user's name should be visible on the homepage
        And I restart the browser session, add cookies and verify successful login