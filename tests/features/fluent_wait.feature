Feature: Fluent Wait - More control over the wait behavior

            | Method           | Behavior                                                             | Use Case                              |
            | ---------------- | -------------------------------------------------------------------- | ------------------------------------- |
            | `time.sleep(10)` | Waits blindly for 10 seconds, even if element is ready earlier       | ❌ Wasteful and unreliable             |
            | `WebDriverWait`  | Waits for a specific condition with default polling every 0.5 sec    | ✅ Great for most cases                |
            | `FluentWait`     | Like WebDriverWait, but **customizable**: poll frequency, exceptions | ✅ Advanced control over wait strategy |

    You need Fluent Wait when:
    👉 Timing is uncertain
    👉 You want smarter retry logic
    👉 You want to poll repeatedly for a condition without over-waiting
    👉 You need control over the waiting behavior

    @fluent_wait
    Scenario: Wait for the input field to become enabled using Fluent Wait
        Given I open the website "https://the-internet.herokuapp.com/dynamic_controls"
        When I click on the Enable button
        Then I wait for the input field to be enabled using Fluent Wait
        And I type "Hello world" into the input field
