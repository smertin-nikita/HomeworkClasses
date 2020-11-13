import random


class Animal:
    """
    Represents animal behavior
    """

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def eat(self, food_weight=0.1):
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

    def __init__(self, name, weight=100):
        super().__init__(name, weight)

    def sound(self):
        print('Му')

    def interaction(self):
        """Human interaction with cow. return volume of milk in litres"""
        volume = random.randint(1, 10)
        print(f'Корова принесла {volume} литров молока')
        return volume


class Goat(Animal):
    """
    Represents Goat behavior
    """

    def __init__(self, name, weight=50):
        super().__init__(name, weight)

    def sound(self):
        print('Ме')

    def interaction(self):
        """Human interaction with Goat. return volume of milk in litres"""
        volume = random.randint(1, 5)
        print(f'Коза принесла {volume} литров молока')
        return volume


class Sheep(Animal):
    """
    Represents Sheep behavior
    """

    def __init__(self, name, weight=40):
        super().__init__(name, weight)

    def sound(self):
        print('Бе')

    def interaction(self):
        """Human interaction with Sheep. return mass of wool in grams"""
        mass = random.randint(500, 1000)
        print(f'С овцы состригли {mass} грамм шерсти')
        return mass


class Goose(Animal):
    """
    Represents Goose behavior
    """

    def __init__(self, name, weight=6):
        super().__init__(name, weight)

    def sound(self):
        print('Гх')

    def interaction(self):
        """Human interaction with Goose. return count of eggs"""
        eggs_cnt = random.randint(1, 4)
        print(f'Гусь снес {eggs_cnt} яйца')
        return eggs_cnt


class Duck(Animal):
    """
    Represents Duck behavior
    """

    def __init__(self, name, weight=4):
        super().__init__(name, weight)

    def sound(self):
        print('Кря')

    def interaction(self):
        """Human interaction with Duck. return count of eggs"""
        eggs_cnt = random.randint(1, 3)
        print(f'Гусь снес {eggs_cnt} яйца')
        return eggs_cnt


class Chicken(Animal):
    """
    Represents Chicken behavior
    """

    def __init__(self, name, weight=5):
        super().__init__(name, weight)

    def sound(self):
        print('Кудах')

    def interaction(self):
        """Human interaction with Chicken. return count of eggs"""
        eggs_cnt = random.randint(1, 5)
        print(f'Гусь снес {eggs_cnt} яйца')
        return eggs_cnt


def feedAnimals(*animals, count_feed=0.3):
    for animal in animals:
        animal.eat(count_feed)


def actions(*animals):
    for animal in animals:
        animal.sound()
        animal.interaction()


animals = [
    Goose('Серый'),
    Goose('Белый'),
    Cow('Манька'),
    Sheep('Барашек'),
    Sheep('Кудрявый'),
    Chicken('Ко-Ко'),
    Chicken('Кукареку'),
    Goat('Рога'),
    Goat('Копыта'),
    Duck('Кряква')
]

# Покормить всех
feedAnimals(*animals)
# Взаимодейстие
actions(*animals)

# get weights of all animals
animals_weight = (animal.weight for animal in animals)
# find sum of weights
print(sum(animals_weight))

# Sort to find the first the most weight animal
animal_weightest = sorted(animals, key=lambda animal: animal.weight, reverse=True)
print(animal_weightest[0].name)
