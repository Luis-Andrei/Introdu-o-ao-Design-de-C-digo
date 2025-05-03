import pytest
from src.services.calculator_4_service import calculate_average

def test_calculate_average_with_valid_numbers():
    numbers = [1, 2, 3, 4, 5]
    result = calculate_average(numbers)
    assert result == 3.0

def test_calculate_average_with_float_numbers():
    numbers = [1.5, 2.5, 3.5]
    result = calculate_average(numbers)
    assert result == 2.5

def test_calculate_average_with_invalid_numbers():
    with pytest.raises(ValueError):
        calculate_average([1, 2, '3', 4]) 