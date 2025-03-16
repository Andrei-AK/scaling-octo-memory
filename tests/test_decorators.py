from src.decorators import log


def test_log_with_capsys(capsys):
    @log()
    def my_function():
        return "1"

    my_function()
    captured = capsys.readouterr()
    assert (
        captured.out
        == "my_function ok\n\n"
    )


def test_log():
    @log()
    def my_function(x, y):
        return x + y

    result = my_function(1, 2)
    assert result == 3

    @log(filename="test_log.txt")
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    with open("test_log.txt", "r", encoding="UTF-8") as f:
        str_in_file = f.read()
    assert "my_function ok\n" in str_in_file

    @log(filename="test_log.txt")
    def my_function(x, y):
        return x + y

    my_function("a", 2)
    with open("test_log.txt", "r", encoding="UTF-8") as f:
        str_in_file = f.read()
    assert ("my_function error: can only concatenate str (not " + '"' +'int'+ '"'+') to str. Inputs: ('+"'"+'a'+"'"+", 2), {}"
        in str_in_file
    )
