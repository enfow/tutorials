"""Define test codes."""

import pytest
from unittest.mock import patch

from src.human import Person, Man, Woman, Baby


#############################################
###        Test with setup_method         ###
#############################################


class TestHuman:
    def setup_method(self):
        self.height, self.weight = 183.0, 72.4
        self.person = Person(height=self.height, weight=self.weight)

    def test_person_init(self):

        assert self.person.height == self.height
        assert self.person.weight == self.weight

    def test_person_eat(self):
        self.person.eat()

        assert self.person.weight == (self.weight + 1)

    def test_person_exercise(self):
        self.person.exercise()

        assert self.person.weight == (self.weight - 1)


#############################################
###       Test with pytest.fixture        ###
#############################################

HEIGHT = 183.0
WEIGHT = 72.4


@pytest.fixture
def mock_man():
    """get mock_man."""
    return Man(HEIGHT, WEIGHT)


class TestMan:

    # pass param with fixture method.
    def test_man_init(self, mock_man):

        assert mock_man.height == HEIGHT
        assert mock_man.weight == WEIGHT

    def test_man_eat(self, mock_man):
        mock_man.eat()

        assert mock_man.weight == (WEIGHT + 1)

    def test_man_exercise(self, mock_man):
        mock_man.exercise()

        assert mock_man.weight == (WEIGHT - 1)


#############################################
###  Test with pytest.mark.parameterize   ###
#############################################


# pass param with parametrize decorator.
@pytest.mark.parametrize(
    "weight,height",  # single string parsing with ","
    [
        (160.0, 52.0),
        (170.0, 58.0),
        (150.0, 47.0),
    ],  # three tuple -> generate 3 test case per 1 test method
)
class TestWoman:
    def test_woman_init(self, height, weight):

        woman = Woman(height, weight)

        assert woman.height == height
        assert woman.weight == weight

    def test_woman_eat(self, height, weight):

        woman = Woman(height, weight)
        woman.eat()
        assert woman.weight == (weight + 1)

    def test_woman_exercise(self, height, weight):
        woman = Woman(height, weight)
        woman.exercise()
        assert woman.weight == (weight - 1)


#############################################
###     Test with unittest.mock.patch     ###
#############################################


class TestBaby:
    """
    Note:
    - Definition of Baby()

        class Baby(Person):
            def __init__(self):
                Person.__init__(self, height=36.2, weight=3.8)

            def sleep(self):
                time.sleep(3)  <- It takes 3 second to execute
                return True
    """

    # patch time.sleep -> mocking time.sleep()
    #                  -> the method time.sleep(3) in the baby.sleep() does not execute
    #                  -> it just return True. So it does not take 3 sec to execute.
    @patch("time.sleep")
    def test_sleep_with_patch(self, mock_sleep):
        mock_sleep.return_value = True

        baby = Baby()
        assert baby.sleep()

    # It takes 3 sec to execute.
    def test_sleep_without_patch(self):

        baby = Baby()
        assert baby.sleep()
