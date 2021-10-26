import pytest
from leapyear import isLeapYear



def test_year_divisible_by_four_and_not_hundred_is_leapyear():
    """Testing if a number can be divided by 4 and not by 100. Then it's a leap year"""
    assert isLeapYear(2004) == True
    assert isLeapYear(2024) == True


def test_year_divisible_by_fourhundred_is_leapyear():
    """Testing if a number can be divided by 400. Then it's a leap year"""
    assert isLeapYear(2000) == True
    assert isLeapYear(1600) == True


def test_year_not_divisible_by_four_is_not_leapyear():
    """Testing if a number is not a multiply of 4. Then it's not a leap year"""
    assert isLeapYear(1801) == False
    assert isLeapYear(2021) == False


def test_year_divisible_by_hundred_but_not_fourhundred_is_not_leapyear():
    """Testing if a number is a multiply of 100, but not 400. Then it's not a leap year"""
    assert isLeapYear(1800) == False
    assert isLeapYear(1700) == False

# # Testing for both of the acceptance criteria
# @pytest.mark.parametrize("year, rest",
#                          [
#                              (2000, 0),
#                              (2024, 0),
#                              (2028, 0)
#                          ]
#                          )
# def test_is_leapYear(year, rest):
#     assert isLeapYear(year) % 4 == rest and isLeapYear(year) % 100 != rest or year % 400 == rest
