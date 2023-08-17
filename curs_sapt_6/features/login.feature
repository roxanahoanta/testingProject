Feature: tests for login page
  Scenario: negative scenario
    Given I am on the login page
    When I click the cookie button
    When I insert the email "testcase1@yahoo.com"
    When I insert the password "ggch6476"
    When I click the loggin button
    Then I see no account error displayed
