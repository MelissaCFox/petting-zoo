from Movements import Walking, Slithering, Swimming

class Attraction:

    def __init__(self, name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()

    def add(self, animal):
        self.animals.append(animal)

    def remove(self, animal):
        self.animals.remove(animal)

    def __str__(self):
        return f'{self.attraction_name} ({len(self)} animals) is {self.description}'

    def __len__(self):
        return len(self.animals)

    @property
    def last_critter_added(self):
        return self.animals[-1]


class PettingZoo(Attraction):

    def __init__(self, name, description):
        super().__init__(name, description)

    def add(self, animal):
        if isinstance(animal, Walking):
            self.animals.append(animal)
            print(f'{animal} that now lives in {self.attraction_name}')
        else:
            print(f'{animal} that would rather not be pet, please do not place them in the {self.attraction_name}.')

class SnakePit(Attraction):

    def __init__(self, name, description):
        super().__init__(name, description)

    def add(self, animal):
        if isinstance(animal, Slithering):
            self.animals.append(animal)
            print(f'{animal} that now lives in {self.attraction_name}')
        else:
            print(f'{animal} that is scared of legless creatures, please do not place them the {self.attraction_name}.')


class Wetlands(Attraction):

    def __init__(self, name, description):
        super().__init__(name, description)

    def add(self, animal):
        if isinstance(animal, Swimming):
            self.animals.append(animal)
            print(f'{animal} that now lives in {self.attraction_name}')
        else:
            print(f'{animal} that cannot swim, please do not place them in the {self.attraction_name}!')