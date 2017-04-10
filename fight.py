# let's make strange creatures to fight with
class Creature:
    def __init__(self, species, strength, health):
        self.species = species
        self.strength = strength
        self.health = health

    def hit(self, creature):
        print "{} hits {}".format(self.species, creature.species)
        creature.health = creature.health - self.strength
        print creature.status()

    def status(self):
        return "{} has {} health.".format(self.species, self.health)

    def is_alive(self):
        return self.health > 0

data = [
    ["dragon", 22, 100  ],
    ["robot",7 ,120  ],
    ["alien", 20, 60  ],
    ["pansinator", 5, 30 ],
    ["wolf",18, 80 ],
]

creatures = []

for d in data:
    c = Creature(d[0], d[1], d[2])
    creatures.append(c)

creatures[0].hit(creatures[1])
#how would I make it random??? e.g.dragon hits robot-robot has 98 health. Robot  hits dragon-dragon has 93 health. moves=dogesand hit
