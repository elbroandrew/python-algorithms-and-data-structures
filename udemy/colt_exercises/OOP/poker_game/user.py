class User:
    active_users = 0

    def __init__(self, first_name: str, last_name: str, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        User.active_users += 1

    def logout(self):
        User.active_users -= 1
        print(f"{self.first_name} has logged out.")

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def initials(self):
        return f"{self.first_name[0].upper()}.{self.last_name[0].upper()}."



u = User('john', "Doe", 34)
print(u.initials())