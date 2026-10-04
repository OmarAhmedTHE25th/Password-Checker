import pytest
from checker import strength_checker, check_breach

def test_strength_checker_strong():
    # Strong password: 12+ chars, upper, lower, number, special
    strong, checks = strength_checker("StrongPass123!")
    assert strong is True
    assert all(checks.values())

def test_strength_checker_weak_length():
    # Weak: too short
    strong, checks = strength_checker("S1!a")
    assert strong is False
    assert checks["At least 12 characters"] is False

def test_strength_checker_weak_no_upper():
    strong, checks = strength_checker("weakpass123!")
    assert strong is False
    assert checks["Has upper case"] is False

def test_strength_checker_weak_no_lower():
    strong, checks = strength_checker("WEAKPASS123!")
    assert strong is False
    assert checks["Has lower case"] is False

def test_strength_checker_weak_no_number():
    strong, checks = strength_checker("WeakPass!!!!")
    assert strong is False
    assert checks["Has numbers"] is False

def test_strength_checker_weak_no_special():
    strong, checks = strength_checker("WeakPass1234")
    assert strong is False
    assert checks["Has special characters"] is False

def test_check_breach_pwned(mocker):
    # Mocking requests.get to simulate a pwned password
    # SHA1 of "password123" is CBFDAC6008F9CAB4083784CBD1874F76618D2A97
    # Prefix: CBFDA, Suffix: C6008F9CAB4083784CBD1874F76618D2A97
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.text = "C6008F9CAB4083784CBD1874F76618D2A97:10\nABCDEF:5"
    mocker.patch("requests.get", return_value=mock_response)
    
    count = check_breach("password123")
    assert count == 10

def test_check_breach_not_pwned(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.text = "ABCDEF:5\n123456:100"
    mocker.patch("requests.get", return_value=mock_response)
    
    count = check_breach("unique_password_999!")
    assert count == 0

def test_check_breach_error(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 404
    mocker.patch("requests.get", return_value=mock_response)
    
    with pytest.raises(RuntimeError, match="Error fetching data: 404"):
        check_breach("password123")
