from datetime import date
from Movements import Slithering, Swimming


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

class Hellbender(Animal, Slithering):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True

class Legless_Lizard(Animal, Slithering):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True

class Salamander(Animal, Slithering, Swimming):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True

class Snake(Animal, Slithering):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True

class Worm(Animal, Slithering):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True