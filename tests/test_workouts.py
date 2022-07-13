import pytest

from workouts import print_workout_days


@pytest.mark.parametrize("test_input,expected", [
            [ 'upper body #1', 'mon\n'.title()],
            ['lower body #1', 'tue\n'.title()],
            ['30 min cardio', 'wed\n'.title()],
            [ 'upper body #2', 'thu\n'.title()],
            ['lower body #2', 'fri\n'.title()],
            [ 'upper body ', 'mon, thu\n'.title()],
            ['lower body ', 'tue, fri\n'.title()],
            ['30 min cardio', 'wed\n'.title()],
            [ 'upper body', 'mon, thu\n'.title()],
            ['lower body', 'tue, fri\n'.title()],
            ['bla', 'No matching workout\n']
        ])
def test_print_workout_days(test_input, expected, capsys):
    print_workout_days(test_input)
    out, err = capsys.readouterr()
    assert out == expected
