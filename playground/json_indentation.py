import json

data = {
    "users": [
        {"Name": "Player1", "skill": 100, "gold": 9999, "weapon": "sword"},
        {"Name": "Player2", "skill": 1, "gold": -1000, "weapon": None},
    ]
}

with open("demo.json", "w") as f:
    json.dump(data, f, indent=2) # indent - делает человекочитаемым json файл
