from udemy.colt_exercises.OOP.poker_game.user import User


class Moderator(User):
    def __init__(self, first, last, age, community):
        super().__init__(first, last, age)
        self.community = community

    def remove_post(self):
        return f"{self.full_name()} removed a post from the {self.community} community."


jasmine = Moderator("Jasmine", "O'Conner", 23, "Piano")
print(jasmine.remove_post())
