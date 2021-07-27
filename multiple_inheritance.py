

class Color():
    def __init__(self, color):
        self.color = color
    
    def print_color(self):
        print(self.color)


class Fish():
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        print(self.name)


# multiple inheritance

class ColoredFish(Fish, Color):
    def __init__(self, name, color):
        Fish.__init__(self, name)
        Color.__init__(self, color)

colored_fish = ColoredFish("woopsy", "green")
colored_fish.print_color()
colored_fish.get_name()

