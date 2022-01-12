from datetime import date
from Movements import Walking, Swimming


class Animal:
    def __init__(self, name, species, food, chip_num):
        self.name = name
        self.species = species
        self.food = food
        self.__chip_number = chip_num
        self.date_added = date.today()

    def __str__(self):
        return f'{self.name} is a {self.species}'

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    @property
    def chip_number(self):
        return self.__chip_number

    @chip_number.setter
    def chip_number(self, num):
        pass


class Goose(Animal, Walking, Swimming):

    def __init__(self, name, species, food, chip_num):
        # No more super() when initializing multiple base classes
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)
        Walking.__init__(self)
        # no more self.swimming = True
    
    def honk(self): 
        print(f"{self.name} honks. A lot")

    def run(self):
        print(f'{self.name} waddles quickly.')


class Alpaca(Animal, Walking):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift  # stays on because not all animals have shifts
        self.walking = True


class Goat(Animal, Walking):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift  # stays on because not all animals have shifts
        self.walking = True


class Pig(Animal, Walking):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift  # stays on because not all animals have shifts
        self.walking = True


class Sheep(Animal, Walking):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift  # stays on because not all animals have shifts
        self.walking = True


class Tortoise(Animal, Walking):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift  # stays on because not all animals have shifts
        self.walking = True

    def feed(self):
        print(f'{self.name} was fed {self.food} in a non-tippable bowl on {date.today().strftime("%m/%d/%Y")}')
