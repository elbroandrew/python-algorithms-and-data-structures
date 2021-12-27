'''tuple'''


def sum_all(*args): # это собирает в аргс со звездочкой
    print(args)
    total = 0
    for n in args:
        total += n
    print(total)


nums = [1,2,3,4,5]
sum_all(*num) # это разбирает переданный список. Так же можно тюпл.

'''dict'''

def add_numbers(a,b,c):
    return a+b+c

data = dict(a=1, b=2, c=3)
add_numbers(**data) # 7

