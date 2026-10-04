# PasswordChecker

A simple Python-based tool to check password strength and identify if a password has been compromised in known data breaches.

## Overview

PasswordChecker provides two main functionalities:
1.  **Strength Checker**: Validates a password against common complexity requirements (length, uppercase, lowercase, numbers, and special characters).
2.  **Breach Checker**: Uses the [Have I Been Pwned](https://haveibeenpwned.com/API/v3#PwnedPasswords) API to check if the password appears in known data breaches using k-Anonymity for security.

## Requirements

-   **Language**: Python 3.x (Tested with 3.12)
-   **Dependencies**: 
    -   `requests`
    -   `pytest` (for testing)
    -   `pytest-mock` (for testing)

## Setup

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/OmarAhmedTHE25th/Password-Strength-Checker.git
    cd PasswordChecker
    ```

2.  **Create and activate a virtual environment** (optional but recommended):
    ```bash
    python -m venv .venv
    # On Windows:
    .venv\Scripts\activate
    # On macOS/Linux:
    source .venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Run Commands

To run the password checker, execute the `checker.py` script:

```bash
python checker.py
```

Follow the prompt to enter a password for evaluation.

## Scripts

Currently, the project uses a single entry point:
-   `checker.py`: The main script that performs strength and breach checks.

## Env Vars

No environment variables are currently required for this project.

## Tests

Automated tests are provided using `pytest`. To run the tests:

```bash
pytest
```

The tests cover:
- Password strength validation logic.
- API integration for breach checking (using mocks).

## Project Structure

```text
PasswordChecker/
├── .idea/           # IDE configuration
├── .venv/            # Virtual environment (ignored by VCS)
├── tests/           # Automated tests
├── checker.py        # Main application script
├── LICENSE           # MIT License
├── README.md         # Project documentation
└── requirements.txt  # Project dependencies
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
