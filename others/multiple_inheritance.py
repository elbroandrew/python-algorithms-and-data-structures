

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

# 1 способ
# class ColoredFish(Fish, Color):
#     def __init__(self, name, color):
#         Fish.__init__(self, name)
#         Color.__init__(self, color)

# colored_fish = ColoredFish("woopsy", "green")
# colored_fish.print_color()
# colored_fish.get_name()

# 2 способ c super()
'''
каждый следующий класс делегируется другому 

class Combined(First, Second, Third):
    def __init__(self):
        super().__init__()
        super(First, self).__init__()
        super(Second, self).__init__()

и так дальше.
'''
class ColoredFish(Fish, Color):
    def __init__(self, name, color):
        super().__init__(name)
        super(Fish, self).__init__(color)

colored_fish = ColoredFish("woopsy", "green")
colored_fish.print_color()
colored_fish.get_name()
