import allure
from utils.api_client import APIClient


def before_all(context):
    context.client = APIClient()
    print("\n🚀 Test Suite Started")


def after_all(context):
    print("\n✅ Test Suite Completed")


def before_scenario(context, scenario):
    print(f"\n▶ Running: {scenario.name}")
    print(f"   Tags: {scenario.tags}")


def after_scenario(context, scenario):
    if scenario.status == "failed":
        print(f"\n❌ Failed: {scenario.name}")
        with allure.step("Scenario failed — capturing details"):
            allure.attach(
                str(scenario.name),
                name="Failed Scenario",
                attachment_type=allure.attachment_type.TEXT
            )
    else:
        print(f"\n✅ Passed: {scenario.name}")


def before_feature(context, feature):
    print(f"\n📂 Feature: {feature.name}")


def after_feature(context, feature):
    print(f"\n📂 Feature Completed: {feature.name}")