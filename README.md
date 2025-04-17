# Bat-Tech Testing Assignment

This repository contains the implementation of test cases for Batman's tech systems using pytest. The tests cover various aspects of the Bat-Tech software, ensuring reliability and functionality of critical components.

## Project Structure

- `bat_functions.py`: Contains the core functions being tested
- `test_bat_functions.py`: Contains all test cases
- `.github/workflows/pytest.yml`: GitHub Actions workflow for continuous integration

## Test Implementation

### Exercise 1: Basic Tests and Parametrization
- Implemented basic tests for `calculate_bat_power` function
- Used pytest parametrization for testing `signal_strength` with various distances

### Exercise 2: Using Fixtures
- Created a fixture for bat vehicles data
- Implemented tests for `get_bat_vehicle` function using the fixture
- Added error handling tests for unknown vehicles

### Exercise 3: Mocking External Dependencies
- Implemented mocking for `fetch_joker_info` function
- Used monkeypatch to avoid actual network delays
- Created custom mock responses for testing

## Running Tests

To run the tests locally:

```bash
pip install pytest
pytest test_bat_functions.py -v
```

## Continuous Integration

The project uses GitHub Actions to automatically run tests on:
- Every push to the main branch
- Every pull request to the main branch

Tests run on Ubuntu with Python 3.9 and 3.10.

## Test Coverage

The test suite covers:
- Basic function functionality
- Edge cases
- Error handling
- External dependency mocking
- Various input parameters

## Contributing

Feel free to submit issues and enhancement requests! 