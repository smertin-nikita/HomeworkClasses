

class Animal:
    """
    Represents animal behavior
    """

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def makeSound(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Cow(Animal):
    """
    Represents Cow behavior
    """

    def __init__(self, name):
        super().__init__(name)


class Goat(Animal):
    """
    Represents Goat behavior
    """

    def __init__(self, name):
        super().__init__(name)


class Sheep(Animal):
    """
    Represents Sheep behavior
    """

    def __init__(self, name):
        super().__init__(name)


class Goose(Animal):
    """
    Represents Goose behavior
    """

    def __init__(self, name):
        super().__init__(name)


class Duck(Animal):
    """
    Represents Duck behavior
    """

    def __init__(self, name):
        super().__init__(name)


class Chicken(Animal):
    """
    Represents Chicken behavior
    """

    def __init__(self, name):
        super().__init__(name)
