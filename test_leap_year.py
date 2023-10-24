from project.leap_year import is_leap_year

def test_divisible_by_4_but_not_100():
    assert is_leap_year(2024) == True


def test_divisible_by_400():
    assert is_leap_year(2000) == True


def test_not_divisible_by_400():
    assert is_leap_year(2021) == False


def test_divisible_by_100_but_not_400():
    assert is_leap_year(1700) == False


