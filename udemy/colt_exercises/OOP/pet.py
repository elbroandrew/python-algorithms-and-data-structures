class Animal:
    allowed = ['cat', 'dog', 'fish', 'parrot']
    def __init__(self, name, species):
        if species not in Animal.allowed:
            raise ValueError(f"You cant have a {species} pet!")
        self.name = name
        self.species = species


p = Animal('Tiger', 'cat')
print(id(Animal.allowed))


class Cat(Animal):
    def __init__(self, name, species, color):
        super().__init__(name, species)
        self.color = color
