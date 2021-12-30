from udemy.colt_exercises.OOP.poker_game.user import User


class Moderator(User):
    total_mods = 0
    def __init__(self, first, last, age, community):
        super().__init__(first, last, age)
        self.community = community
        Moderator.total_mods += 1

    @classmethod
    def display_active_mods(cls):
        return cls.total_mods

    def remove_post(self):
        return f"{self.full_name()} removed a post from the {self.community} community."


jasmine = Moderator("Jasmine", "O'Conner", 23, "Piano")
print(jasmine.remove_post())
