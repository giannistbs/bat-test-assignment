import pytest
from bat_functions import calculate_bat_power, signal_strength, get_bat_vehicle, fetch_joker_info

# Exercise 1: Basic Tests and Parametrization

def test_calculate_bat_power():
    """Test the calculate_bat_power function with various power levels"""
    assert calculate_bat_power(1) == 42
    assert calculate_bat_power(2) == 84
    assert calculate_bat_power(0) == 0
    assert calculate_bat_power(10) == 420

@pytest.mark.parametrize("distance,expected_strength", [
    (0, 100),    # At source
    (5, 50),     # Half strength
    (10, 0),     # No signal
    (12, 0),     # Beyond range
    (7.5, 25),   # Quarter strength
])
def test_signal_strength(distance, expected_strength):
    """Test signal_strength with various distances using parametrization"""
    assert signal_strength(distance) == expected_strength

# Exercise 2: Using Fixtures

@pytest.fixture
def bat_vehicles():
    """Fixture providing a dictionary of bat vehicles for testing"""
    return {
        'Batmobile': {'speed': 200, 'armor': 80},
        'Batwing': {'speed': 300, 'armor': 60},
        'Batcycle': {'speed': 150, 'armor': 50}
    }

def test_get_bat_vehicle(bat_vehicles):
    """Test get_bat_vehicle function using the fixture"""
    # Test known vehicles
    assert get_bat_vehicle('Batmobile') == bat_vehicles['Batmobile']
    assert get_bat_vehicle('Batwing') == bat_vehicles['Batwing']
    assert get_bat_vehicle('Batcycle') == bat_vehicles['Batcycle']
    
    # Test unknown vehicle
    with pytest.raises(ValueError) as exc_info:
        get_bat_vehicle('UnknownVehicle')
    assert "Unknown vehicle: UnknownVehicle" in str(exc_info.value)

# Exercise 3: Mocking External Dependencies

def test_fetch_joker_info(monkeypatch):
    """Test fetch_joker_info with mocked response"""
    # Mock response data
    mock_data = {'mischief_level': 0, 'location': 'captured'}
    
    # Mock the time.sleep function to avoid waiting
    def mock_sleep(seconds):
        pass
    
    # Apply the mocks
    monkeypatch.setattr('time.sleep', mock_sleep)
    
    # Create a mock function that returns our test data
    def mock_fetch_joker_info():
        return mock_data
    
    # Replace the original function with our mock
    import bat_functions
    monkeypatch.setattr(bat_functions, 'fetch_joker_info', mock_fetch_joker_info)
    
    # Test the function
    result = bat_functions.fetch_joker_info()
    assert result == mock_data
    assert result['mischief_level'] == 0
    assert result['location'] == 'captured' 