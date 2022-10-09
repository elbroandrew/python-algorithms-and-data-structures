"""
names = ["Петров", "Иванов", "Сидов", "Пак"]
output: ["П****в", "И****в", "С***в", "П*к"]
"""

names = ["Петров", "Иванов", "Сидов", "Пак", "Ли"]


def replace_with_asterisks(input_str: str) -> str:
    if len(input_str) == 2:
        return f"{input_str[0]}*"
    elif len(input_str) == 1:
        return input_str
    else:
        return input_str[0] + '*' * (len(input_str) - 2) + input_str[-1]


names = [*map(replace_with_asterisks, names)]

print(names)
