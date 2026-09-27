Feature: User Management API

  @smoke @users
  Scenario: Get all users
    Given the API is available
    When I send a GET request to "/users"
    Then the response status code should be 200
    And the response should contain a list of users

  @smoke @users
  Scenario: Get a single user
    Given the API is available
    When I send a GET request to "/users/1"
    Then the response status code should be 200
    And the response field "name" should be "Leanne Graham"

  @regression @users
  Scenario: Create a new user
    Given the API is available
    When I send a POST request to "/users" with payload
      | name   | email           | username  |
      | Samrat | samrat@test.com | samrat99  |
    Then the response status code should be 201

  @regression @users
  Scenario: Update a user
    Given the API is available
    When I send a PUT request to "/users/1" with payload
      | name           | email              |
      | Samrat Updated | samrat@updated.com |
    Then the response status code should be 200
    And the response field "name" should be "Samrat Updated"

  @regression @users
  Scenario: Delete a user
    Given the API is available
    When I send a DELETE request to "/users/1"
    Then the response status code should be 200

  @negative @users
  Scenario: Get a non-existent user
    Given the API is available
    When I send a GET request to "/users/999"
    Then the response status code should be 404

  @performance @users
  Scenario: Verify response time is acceptable
    Given the API is available
    When I send a GET request to "/users"
    Then the response time should be under 3000 milliseconds

  @regression @users
  Scenario: Verify user response schema
    Given the API is available
    When I send a GET request to "/users/1"
    Then the response status code should be 200
    And the user response schema should be valid

  @regression @users
  Scenario Outline: Get multiple users by ID
    Given the API is available
    When I send a GET request to "/users/<id>"
    Then the response status code should be 200

    Examples:
      | id |
      | 1  |
      | 2  |
      | 3  |