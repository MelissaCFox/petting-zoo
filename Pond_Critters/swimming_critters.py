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


class Beaver(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True


class Duck(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True


class Fish(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True


class Frog(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True


class Turtle(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True
