import pytest

from numbers_to_dec import list_to_decimal


class TestListTODecimal:

    @pytest.mark.parametrize("test_input,expected", [
        ([0, 4, 2, 8], 428),
        ([1, 2], 12),
        ([3], 3),
        ([0, 0, 0, 5], 5),
        ([0], 0)
    ])
    def test_should_work_correctly(self, test_input, expected):
        # given
        obtained = list_to_decimal(test_input)
        assert obtained == expected

    @pytest.mark.parametrize("test_input", [
        [-3, 12],
        [12],
        [-6],
        [10]
    ])
    def test_value_error(self, test_input):
        with pytest.raises(ValueError):
            list_to_decimal(test_input)

    @pytest.mark.parametrize("test_input", [
        [6, 2, True],
        [3.6, 4, 1],
        ['4', 5, 3, 1]
    ])
    def test_type_error(self, test_input):
        with pytest.raises(TypeError):
            list_to_decimal(test_input)