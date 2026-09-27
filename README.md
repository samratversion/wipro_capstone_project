# Wipro Capstone Project — API Automation Framework

## Student
**Name:** Samrat  
**College:** UEM  
**Capstone:** Assignment 3 — Python API Automation Framework

---

## Repository Structure

| Folder | Contents |
|---|---|
| `api-automation-framework/` | Main capstone project — Behave BDD + Requests + Allure |
| `assignments/` | Additional Python assignment files |
| `certificates/` | Course completion certificates |
| `video/` | Project demo video |

---

## How to Run the Project

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run tests
```bash
behave -f allure_behave.formatter:AllureFormatter -o reports
```

### Generate Allure report
```bash
allure serve reports
```

---

## Tech Stack
- Python 3
- Requests Library
- Behave BDD
- Allure Reporting
- JSONPlaceholder API
- AutomationExercise API

---

## Test Coverage
- 15 test scenarios
- 100% pass rate
- Positive, Negative, Performance and Schema validation tests
- Authentication API testing
- Data Driven Testing using Scenario Outline
