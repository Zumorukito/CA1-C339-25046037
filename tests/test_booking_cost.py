import pytest
from src.booking_cost import calculate_booking_cost


@pytest.mark.parametrize("nights, rate, expected_result", [
    (1, 10000, 10000),
    (3, 10000, 30000),
    (6, 10000, 60000),
    (7, 10000, 70000),
    (30, 10000, 300000),
    (2, 0, 0),
])

def test_booking_cost_returns_expected_result(nights, rate, expected_result):
    result = calculate_booking_cost(nights, rate)
    assert result == expected_result
    assert type(result) is int


@pytest.mark.parametrize("nights, rate, error", [
    (0, 10000, ValueError),
    (-1, 10000, ValueError),
    (31, 10000, ValueError),
    (2, -1, ValueError),
    ("2", 10000, TypeError),
    (2.0, 10000, TypeError),
    (True, 10000, TypeError),
    (None, 10000, TypeError),
    (2, "10000", TypeError),
    (2, 10000.0, TypeError),
    (2, False, TypeError),
    (2, None, TypeError),
])

def test_booking_cost_invalid_input_raises_error(nights, rate, error):
    with pytest.raises(error):
        calculate_booking_cost(nights, rate)