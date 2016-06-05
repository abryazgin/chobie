Feature: Check login page

  Scenario: Have access for registered user
    Given I am a some registered user
    When I try login
    Then I succesfully login

  Scenario: Access denied for registered user when user enter bad password
    Given I am a some registered user
    When I try login with incorrect password
    Then I don't login

  Scenario: Have access for registered user
    Given I am a some unregistered user
    When I try login
    Then I don't login