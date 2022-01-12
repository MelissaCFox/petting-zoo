from Petting_Critters import (Alpaca, Goat, Sheep, Pig, Tortoise)
from Tank_Critters import (Hellbender, Legless_Lizard, Salamander, Snake, Worm)
from Pond_Critters import (Beaver, Duck, Fish, Frog, Turtle)
from Attractions import (PettingZoo, SnakePit, Wetlands)

      
kyle = Alpaca("Kyle", "alpaca", "midday", "Mazuri Petting Zoo Diet")
susan = Pig("Susan", "kune kune pig", "morning", "Mazuri Mini Pig Food")

yard = PettingZoo("Barn", "quaint century-old barn with domestic hoofstock")
yard.add(kyle)
yard.add(susan)

for animal in yard.animals:
    print(f'You can find {animal.name} the {animal.species} in the {yard.attraction_name} during the {animal.shift} shift.')