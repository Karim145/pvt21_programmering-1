from Iteration6 import percent_correct

myt = ("271", "408")


def test_precent_correct():  # passed the rest 271/408 i percent
    assert percent_correct(myt) == '66%'


def test_precent_correct_return_string():
    assert type(percent_correct(myt)) is int  # failet the fuction return a string


def test_percent_correct_len_return():
    assert len(percent_correct(myt)) > 3  # failet the function return a string with the len
