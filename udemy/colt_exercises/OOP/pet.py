class Pet:
    allowed = ['cat', 'dog', 'fish', 'parrot']


    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError(f"You cant have a {species} pet!")
        self.name = name
        self.species = species


p = Pet('Tiger', 'cat')
print(id(Pet.allowed))


