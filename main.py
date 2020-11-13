

class Animal:
    """
    Represents animal behavior
    """

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def sound(self):
        """Animal makes a distinct sound"""
        raise NotImplementedError("Subclass must implement abstract method")


class Cow(Animal):
    """
    Represents Cow behavior
    """

    def __init__(self, name, weight):
        super().__init__(name, weight)

    def sound(self):
        print('Му')


class Goat(Animal):
    """
    Represents Goat behavior
    """

    def __init__(self, name, weight):
        super().__init__(name, weight)

    def sound(self):
        print('Ме')


class Sheep(Animal):
    """
    Represents Sheep behavior
    """

    def __init__(self, name, weight):
        super().__init__(name, weight)

    def sound(self):
        print('Бе')


class Goose(Animal):
    """
    Represents Goose behavior
    """

    def __init__(self, name, weight):
        super().__init__(name, weight)

    def sound(self):
        print('Гх')


class Duck(Animal):
    """
    Represents Duck behavior
    """

    def __init__(self, name, weight):
        super().__init__(name, weight)

    def sound(self):
        print('Кря')


class Chicken(Animal):
    """
    Represents Chicken behavior
    """

    def __init__(self, name, weight):
        super().__init__(name, weight)

    def sound(self):
        print('Кудах')
