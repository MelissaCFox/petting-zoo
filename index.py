from Petting_Critters import (Alpaca, Goat, Sheep, Pig, Tortoise)
from Tank_Critters import (Hellbender, Legless_Lizard, Salamander, Snake, Worm)
from Pond_Critters import (Beaver, Duck, Fish, Frog, Turtle)
from Attractions import (PettingZoo, SnakePit, Wetlands)


kyle = Alpaca("Kyle", "alpaca", "midday", "Mazuri Petting Zoo Diet", 123)
susan = Pig("Susan", "kune kune pig", "morning", "Mazuri Mini Pig Food", 467)
becky = Goat("Becky", "Nubian goat", "afternoon",
             "Mazuri Petting Zoo Diet", 459)
duke = Tortoise("Duke", "red-footed tortoise", "midday", "mixed greens", 100)

yard = PettingZoo("Barn", "quaint century-old barn with domestic hoofstock")
yard.add(kyle)
yard.add(susan)
yard.add(becky)


# for animal in yard.animals:
#     print(f'You can find {animal.name} the {animal.species} in the {yard.attraction_name} during the {animal.shift} shift.')

sean = Snake("Sean", "rainbow boa", "mice", 862)
pit = SnakePit("Snake Pit", "lots of snakes happily co-habitating")
pit.add(sean)
# for animal in pit.animals:
#     print(
#         f'You can find {animal.name} the {animal.species} in the {pit.attraction_name}.')

print(duke.feed())
print(becky.feed())