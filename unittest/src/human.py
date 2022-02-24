"""Define class and function for test code example."""
import time


class Person:
    """Define person object."""

    def __init__(self, height: float, weight: float):
        """Initialize."""
        self.height = height
        self.weight = weight

    def eat(self):
        """Eat food."""
        self.weight += 1.0

    def exercise(self):
        """Exercise."""
        self.weight -= 1.0


class Man(Person):
    def __init__(self, height: float, weight: float):
        """Initialize."""
        Person.__init__(self, height, weight)
        self.sex = "male"


class Woman(Person):
    def __init__(self, height: float, weight: float):
        """Initialize."""
        Person.__init__(self, height, weight)
        self.sex = "female"


class Baby(Person):
    def __init__(self):
        """Initialize."""
        Person.__init__(self, height=36.2, weight=3.8)

    def sleep(self):
        """sleep 3 sec."""
        time.sleep(3)
        return True
