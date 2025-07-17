# GithubOrgClient

## 🔍 Overview

**GithubOrgClient** is a Python project that interfaces with the GitHub API to fetch organization and repository information. It includes:
- A class `GithubOrgClient` that wraps GitHub API functionality
- Unit and integration tests using `unittest`, `parameterized`, and `unittest.mock`

This project emphasizes proper testing practices, mocking external API calls, and clean code structure.

---

## 📁 Project Structure
`├── client.py # GithubOrgClient implementation` \
`├── test_client.py # Unit and integration tests`\
`├── utils.py # Utility function get_json()`\
`├── fixtures.py # JSON fixtures used for integration tests`  
`├── README.md # You're reading it`
 

---

## 🚀 Features

- Fetch organization metadata via `https://api.github.com/orgs/{org}`
- Retrieve public repositories for an organization
- Filter repositories by license type
- Comprehensive test suite (unit + integration)
- Mocks external HTTP requests for test reliability

---

## 🧪 Tests

Tests are organized using Python’s `unittest` framework.

### ✅ Unit Tests

Test the behavior of individual components in isolation using:
- `@patch` to mock external dependencies
- `@parameterized.expand` to test with multiple input values

### 🔁 Integration Tests

Test the full flow of `GithubOrgClient.public_repos()` with real fixture data and mocked HTTP requests only.

Fixtures used:
- `org_payload`
- `repos_payload`
- `expected_repos`
- `apache2_repos`

---


### 📜 Example Usage
`from client import GithubOrgClient`

`client = GithubOrgClient("google")
print(client.public_repos())              # All public repos
print(client.public_repos("apache-2.0"))  # Only repos with Apache license`

