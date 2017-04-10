class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return "My name is {} and I am {} years old.".format(self.name, self.age)

    def greet(self, person):
        return "{} says hello to {}".format(self.name, person.name)

# people data
data = [
    ["Mishca Barr", 9],
    ["Akeisha Barr", 6],
    ["Scott Barr", 44],
    ["Sarah Tilley", 42]
]

# let's make an array of people from the data
people = []

# loop over the data
for d in data:
    # make a person from the data
    p = Person(d[0], d[1])

    # the person should introduce itself
    print p.introduce()

    # add the person to the array
    people.append(p)

# make one person say hello to another person
print people[0].greet(people[1])
