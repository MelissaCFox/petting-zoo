from Petting_Critters import (Alpaca, Goat, Sheep, Pig, Tortoise)
from Tank_Critters import (Hellbender, Legless_Lizard, Salamander, Snake, Worm)
from Pond_Critters import (Beaver, Duck, Fish, Frog, Turtle)
from Attractions import (PettingZoo, SnakePit, Wetlands)


kyle = Alpaca("Kyle", "alpaca", "midday", "Mazuri Petting Zoo Diet", 123)
susan = Pig("Susan", "kune kune pig", "morning", "Mazuri Mini Pig Food")
becky = Goat("Becky", "Nubian goat", "afternoon", "Mazuri Petting Zoo Diet")

yard = PettingZoo("Barn", "quaint century-old barn with domestic hoofstock")
yard.add(kyle)
yard.add(susan)
yard.add(becky)


# for animal in yard.animals:
# print(f'You can find {animal.name} the {animal.species} in the {yard.attraction_name} during the {animal.shift} shift.')

# kyle.chip_num = 345
# print(f"{kyle.name}'s chip number is {kyle.chip_num}")

print(yard.last_critter_added)