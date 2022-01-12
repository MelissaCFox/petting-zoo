from Petting_Critters import (Alpaca, Goat, Sheep, Pig, Tortoise)
from Tank_Critters import (Hellbender, Legless_Lizard, Salamander, Snake, Worm)
from Pond_Critters import (Beaver, Duck, Fish, Frog, Turtle)

      
kyle = Alpaca("Kyle", "alpaca", "midday", "Mazuri Petting Zoo Diet")
print(f'{kyle.name} the {kyle.species} is available to pet during the {kyle.shift} shift.')

print(kyle.feed())