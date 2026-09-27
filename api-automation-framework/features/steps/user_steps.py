import allure
from behave import given, when, then
from utils.api_client import APIClient

client = APIClient()


@given("the API is available")
def step_api_available(context):
    context.response = None


@allure.story("Get Users")
@when('I send a GET request to "{endpoint}"')
def step_get_request(context, endpoint):
    with allure.step(f"Sending GET request to {endpoint}"):
        context.response = client.get(endpoint)


@allure.story("Create User")
@when('I send a POST request to "{endpoint}" with payload')
def step_post_request(context, endpoint):
    row = context.table[0]
    payload = {
        "name": row["name"],
        "email": row["email"],
        "username": row["username"]
    }
    with allure.step(f"Sending POST request to {endpoint}"):
        context.response = client.post(endpoint, payload)


@allure.story("Update User")
@when('I send a PUT request to "{endpoint}" with payload')
def step_put_request(context, endpoint):
    row = context.table[0]
    payload = {
        "name": row["name"],
        "email": row["email"]
    }
    with allure.step(f"Sending PUT request to {endpoint}"):
        context.response = client.put(endpoint, payload)


@allure.story("Delete User")
@when('I send a DELETE request to "{endpoint}"')
def step_delete_request(context, endpoint):
    with allure.step(f"Sending DELETE request to {endpoint}"):
        context.response = client.delete(endpoint)


@then("the response status code should be {status_code:d}")
def step_check_status_code(context, status_code):
    with allure.step(f"Verifying status code is {status_code}"):
        assert context.response.status_code == status_code, \
            f"Expected {status_code}, got {context.response.status_code}"


@then("the response should contain a list of users")
def step_check_list(context):
    with allure.step("Verifying response is a non-empty list"):
        data = context.response.json()
        assert isinstance(data, list), "Response is not a list"
        assert len(data) > 0, "User list is empty"


@then('the response field "{field}" should be "{value}"')
def step_check_field(context, field, value):
    with allure.step(f"Verifying field '{field}' equals '{value}'"):
        data = context.response.json()
        assert field in data, f"Field '{field}' not found in response"
        assert str(data[field]) == value, \
            f"Expected '{value}', got '{data[field]}'"


@then("the response time should be under {milliseconds:d} milliseconds")
def step_check_response_time(context, milliseconds):
    with allure.step(f"Verifying response time is under {milliseconds}ms"):
        actual = context.response.elapsed.total_seconds() * 1000
        assert actual < milliseconds, \
            f"Too slow: {actual:.2f}ms (limit: {milliseconds}ms)"


@then("the user response schema should be valid")
def step_validate_schema(context):
    with allure.step("Verifying all required fields are present"):
        data = context.response.json()
        required_fields = [
            "id", "name", "username", "email",
            "address", "phone", "website", "company"
        ]
        for field in required_fields:
            assert field in data, f"Missing field: {field}"