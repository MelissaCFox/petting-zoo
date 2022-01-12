class PettingZoo:

    def __init__(self, name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()

    def add(self, animal):
        self.animals.append(animal)

    @property
    def last_critter_added(self):
        return self.animals[-1]


class SnakePit:

    def __init__(self, name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()

    def add(self, animal):
        self.animals.append(animal)


class Wetlands:

    def __init__(self, name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()

    def add(self, animal):
        self.animals.append(animal)