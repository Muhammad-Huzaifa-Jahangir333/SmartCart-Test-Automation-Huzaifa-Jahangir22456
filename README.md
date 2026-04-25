# SmartCart Test Automation

UI test automation project built with Playwright (Python) and Pytest against the public SauceDemo site.

## Features

- Page Object Model based test design
- End-to-end coverage for login, cart, and checkout flow
- HTML test report generation using pytest-html
- GitHub Actions workflow for automated test execution
- Optional headed mode for live browser demo runs

## Tech Stack

- Python
- Pytest
- Playwright for Python
- GitHub Actions

## Project Structure

```text
Smart-cart-Test-Automation/
├── .github/
│   └── workflows/
│       └── test.yml
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/
│   ├── conftest.py
│   ├── test_login.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   └── test_regression.py
├── utils/
│   └── config.py
├── requirements.txt
├── pytest.ini
└── README.md
```

## Getting Started

### 1. Create and activate a virtual environment

Use your own virtual environment path if you are not using the provided one.

```powershell
.\venv1\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
pip install -r requirements.txt
python -m playwright install chromium
```

## Running Tests

Run all tests:

```powershell
pytest -q
```

Run a specific test module:

```powershell
pytest tests/test_login.py -v
```

Run in headed mode (visible browser):

```powershell
$env:HEADED="1"
pytest -v
```

Run in headed mode with slow motion (demo friendly):

```powershell
$env:HEADED="1"
$env:SLOW_MO_MS="350"
pytest -v
```

## Test Report

- Local HTML report path: `report.html`
- Open local report:

```powershell
start report.html
```

The report file is intentionally ignored in Git and should not be committed.

## Test Coverage

| Test File          | What It Tests                          |
|--------------------|----------------------------------------|
| test_login.py      | Successful login                       |
| test_cart.py       | Add product to cart                    |
| test_checkout.py   | Complete end-to-end checkout flow      |
| test_regression.py | Failed login, locked user, empty field |

## Security Note

Credentials in `utils/config.py` are for the PUBLIC demo site saucedemo.com only.
Never store real passwords in source code.

## CI

GitHub Actions workflow file:

- `.github/workflows/test.yml`

The workflow runs on push and pull request, installs dependencies, installs Chromium, runs tests, and uploads the HTML report as an artifact.

## Notes For Contributors

- Keep test data in `utils/config.py`
- Keep selectors and UI operations inside `pages/`
- Keep assertions and flow logic inside `tests/`
- Avoid committing virtual environments, cache folders, and generated reports

## License

For educational and demonstration use.
