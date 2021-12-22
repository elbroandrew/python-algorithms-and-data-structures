person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
#answer {"name": "Jared", "job": "Musician", "city": "Bern"}

answer = {elem[0]: elem[1] for elem in person}
print(answer)


# SECOND SOLUTION
answer2 = {k: v for k, v in person}
print(answer2)


# 3 SOLUTION
answer3 = dict(person)
