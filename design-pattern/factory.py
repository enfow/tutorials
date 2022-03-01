"""Define factoy method design pattern example."""
from abc import ABC, abstractmethod


class Product(ABC):
    """Define abstract product class."""

    def __init__(self, version: int) -> None:
        """Initialize."""
        self.version = version

    @abstractmethod
    def print_spec(self) -> None:
        """Print the spec of the product."""
        pass


class IPhone(Product):
    """Define concrete product class: IPhone."""

    def print_spec(self) -> None:
        """Print the spec of the iPhone."""
        print(f"iPhone{self.version}, designed by apple in california.")


class Galaxy(Product):
    """Define concrete product class: Galaxy."""

    def print_spec(self) -> None:
        """Print the spec of the iPhone."""
        print(f"Galaxy{self.version}, made in Korea.")


class Factory(ABC):
    """Define abstract factory class."""

    def __init__(self, location: str) -> None:
        """Initialize."""
        self.location = location

    @abstractmethod
    def factory_method(self) -> Product:
        pass

    def make_product(self) -> Product:
        return self.factory_method()


class FactoryInKorea(Factory):
    """Define Factory in Korea class."""

    def __init__(self) -> None:
        """Initailize."""
        Factory.__init__(self, location="Korea")

    def factory_method(self) -> Galaxy:
        return Galaxy(version="22")


class FactoryInAmerica(Factory):
    """Define Factory in Korea class."""

    def __init__(self) -> None:
        """Initailize."""
        Factory.__init__(self, location="USA")

    def factory_method(self) -> Galaxy:
        return IPhone(version="13")


if __name__ == "__main__":
    # Factory in Korea makes GALAXY, SAMSUNG
    factory_in_korea = FactoryInKorea()
    made_in_korea = factory_in_korea.make_product()
    made_in_korea.print_spec()

    # Factory in USA makes iPhone, APPLE
    factory_in_america = FactoryInAmerica()
    made_in_america = factory_in_america.make_product()
    made_in_america.print_spec()
