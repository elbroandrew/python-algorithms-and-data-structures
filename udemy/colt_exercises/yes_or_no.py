'''use generator to yield yes/no'''

'''
gen = yes_or_no()
next(gen) # 'yes'
next(gen) # 'no'
next(gen) # 'yes'
next(gen) # 'no'
'''

def yes_or_no():
    answer = "yes"
    while True:
        yield answer
        answer = "no" if answer == "yes" else "yes"

my_answer = yes_or_no()
print(next(my_answer))
print(next(my_answer))
print(next(my_answer))
print(next(my_answer))
print(next(my_answer))
print(next(my_answer))