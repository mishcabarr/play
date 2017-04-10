# let's make strange aliens
class Creature:
    def __init__(self, creature, colour):
        self.creature = creature
        self.colour = colour

    def introduce(self):
        return "I am a {} and am {}.".format(self.creature, self.colour)

    def greet(self, creature):
        return "{} says hello to {}".format(self.creature, creature.creature)

data = [
    ["dragon", "blue" ],
    ["robot", "grey and red" ],
    ["alien", "green"],
    ["pansinator",  "rainbow"],
    ["spike-tailed-snow-wolf", "grey,black and green"],
]

creatures = []

for d in data:
    c = Creature(d[0], d[1])
    # print c.introduce()
    creatures.append(c)

print creatures[0].greet(creatures[1])
