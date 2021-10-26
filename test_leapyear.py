import pytest
from leapyear import isLeapYear


# Testing each acceptance criteria
def test_leapyear_divide_four_and_not_hundred():
    """Testing if a number can be divided by 4 and not by 100. Then it's a leap year"""
    year = isLeapYear(2004)
    assert year % 4 == 0 and year % 100 != 0


def test_leapyear_divide_fourhundred():
    """Testing if a number can be divided by 400. Then it's a leap year"""
    year = isLeapYear(2000)
    assert year % 400 == 0


def test_not_leapyear_dont_divide_four():
    """Testing if a number is not a multiply of 4. Then it's not a leap year"""
    year = isLeapYear(1801)
    assert year % 4 != 0


def test_not_leapyear_divide_hundred_and_not_fourhundred():
    """Testing if a number is a multiply of 100, but not 400. Then it's not a leap year"""
    year = isLeapYear(1800)
    assert year % 100 == 0 and year % 400 != 0


@pytest.mark.parametrize(
    # A list of different years that get used to test if a year is a leap year
    "year",
    [
        2000,
        2020,
        2024,
        2028,
    ],
)
class TestGroupLeapYear:
    """A class for testing leap year, with a common parameter "year"."""

    def test_divide_four_and_not_hundred(self, year):
        """This will return True if it's a multiply of 4 but not 100"""
        return year % 4 == 0 and year % 100 != 0

    def test_divide_four_hundred(self, year):
        """This will return True if it's a multiply of 400"""
        return year % 400 == 0

    def test_divide(self, year):
        """Testing if one of the functions are true. Then it's a leap year"""
        assert isLeapYear(self.test_divide_four_hundred(year)) \
               or isLeapYear(self.test_divide_four_and_not_hundred(year))

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
