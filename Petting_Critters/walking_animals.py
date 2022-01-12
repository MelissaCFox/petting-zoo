from datetime import date


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


class Alpaca(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift  # stays on because not all animals have shifts
        self.walking = True


class Goat(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift  # stays on because not all animals have shifts
        self.walking = True


class Pig(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift  # stays on because not all animals have shifts
        self.walking = True


class Sheep(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift  # stays on because not all animals have shifts
        self.walking = True


class Tortoise(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift  # stays on because not all animals have shifts
        self.walking = True

    def feed(self):
        print(f'{self.name} was fed {self.food} in a non-tippable bowl on {date.today().strftime("%m/%d/%Y")}')
