from src import decorators


def test_log(capsys, successful_completion):
    decorators.sum_numbers(successful_completion[1], successful_completion[2])
    captured = capsys.readouterr()
    assert successful_completion[0] == captured.out
