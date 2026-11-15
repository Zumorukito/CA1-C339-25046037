import pytest
from src.booking_refund import is_refundable


@pytest.mark.parametrize("hours, flexible, expected_result", [
    (0, True, False),
    (47, True, False),
    (48, True, True),
    (49, True, True),
    (0, False, False),
    (47, False, False),
    (48, False, False),
    (49, False, False),
])
def test_refund_returns_expected_result(hours, flexible, expected_result):
    result = is_refundable(hours, flexible)
    assert result is expected_result


@pytest.mark.parametrize("hours, flexible, error", [
    (-1, True, ValueError),
    (-1, False, ValueError),
    ("48", True, TypeError),
    (48.0, True, TypeError),
    (True, True, TypeError),
    (None, True, TypeError),
    (48, "True", TypeError),
    (48, 1, TypeError),
    (48, 0, TypeError),
    (48, None, TypeError),
])
def test_refund_invalid_input_raises_error(hours, flexible, error):
    with pytest.raises(error):
        is_refundable(hours, flexible)