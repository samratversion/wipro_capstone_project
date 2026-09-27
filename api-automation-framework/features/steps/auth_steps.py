import allure
from behave import given, when, then
from utils.api_client import APIClient

client = APIClient()


@given("the auth API is available")
def step_auth_api_available(context):
    context.auth_response = None


@when("I send a POST request to login with:")
def step_auth_login(context):
    row = context.table[0]
    payload = {
        "email": row["email"],
        "password": row["password"]
    }
    with allure.step(f"Logging in with email: {row['email']}"):
        context.auth_response = client.auth_post("/api/verifylogin", payload)


@then("the auth response status code should be {status_code:d}")
def step_auth_status_code(context, status_code):
    assert context.auth_response.status_code == status_code, \
        f"Expected {status_code}, got {context.auth_response.status_code}"


@then("the auth response should indicate failure")
def step_auth_failure(context):
    data = context.auth_response.json()
    assert data["responseCode"] != 200, \
        f"Expected failure but got responseCode: {data['responseCode']}"