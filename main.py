import random


class Animal:
    """
    Represents animal behavior
    """

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def feed(self, food_weight=0.1):
        self.weight += food_weight

    def sound(self):
        """Animal makes a distinct sound"""
        raise NotImplementedError("Subclass must implement abstract method")

    def interaction(self):
        """Human interaction with animal"""
        raise NotImplementedError("Subclass must implement abstract method")


class Cow(Animal):
    """
    Represents Cow behavior
    """

    def __init__(self, name, weight):
        super().__init__(name, weight)

    def sound(self):
        print('Му')

    def interaction(self):
        """Human interaction with cow. return volume of milk in litres"""
        return random.randint(1, 10)


class Goat(Animal):
    """
    Represents Goat behavior
    """

    def __init__(self, name, weight):
        super().__init__(name, weight)

    def sound(self):
        print('Ме')

    def interaction(self):
        """Human interaction with Goat. return volume of milk in litres"""
        return random.randint(1, 5)


class Sheep(Animal):
    """
    Represents Sheep behavior
    """

    def __init__(self, name, weight):
        super().__init__(name, weight)

    def sound(self):
        print('Бе')

    def interaction(self):
        """Human interaction with Sheep. return mass of wool in grams"""
        return random.randint(500, 1000)


class Goose(Animal):
    """
    Represents Goose behavior
    """

    def __init__(self, name, weight):
        super().__init__(name, weight)

    def sound(self):
        print('Гх')

    def interaction(self):
        """Human interaction with Goose. return count of eggs"""
        return random.randint(1, 4)


class Duck(Animal):
    """
    Represents Duck behavior
    """

    def __init__(self, name, weight):
        super().__init__(name, weight)

    def sound(self):
        print('Кря')

    def interaction(self):
        """Human interaction with Duck. return count of eggs"""
        return random.randint(1, 3)


class Chicken(Animal):
    """
    Represents Chicken behavior
    """

    def __init__(self, name, weight):
        super().__init__(name, weight)

    def sound(self):
        print('Кудах')

    def interaction(self):
        """Human interaction with Chicken. return count of eggs"""
        return random.randint(1, 5)
