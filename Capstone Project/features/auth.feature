Feature: Authentication API

  # automationexercise.com/api/verifyLogin returns:
  # 200 → registered user exists
  # 404 → user not found / invalid credentials

  @negative @auth
  Scenario: Login with invalid credentials
    Given the auth API is available
    When I send a POST request to login with:
      | email               | password  |
      | invalid@example.com | wrongpass |
    Then the auth response status code should be 404

  @negative @auth
  Scenario: Login with missing password
    Given the auth API is available
    When I send a POST request to login with:
      | email               | password |
      | invalid@example.com |          |
    Then the auth response status code should be 404

  @smoke @auth
  Scenario: Verify login endpoint is reachable
    Given the auth API is available
    When I send a POST request to login with:
      | email               | password  |
      | invalid@example.com | wrongpass |
    Then the auth response status code should be 404

  @smoke @auth
  Scenario: Login with valid credentials returns user not found
    Given the auth API is available
    When I send a POST request to login with:
      | email                | password |
      | test@example.com     | test123  |
    Then the auth response status code should be 404