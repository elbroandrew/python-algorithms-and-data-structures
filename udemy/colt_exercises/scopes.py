'''
В пайтоне 5 типов скоупов:
LEGB Rule (где ищет поочереди):
1. Local
2. Enclosing
3. Global
4. Built-in
'''

# GLOBAL
x = 'This is global level'


# LOCAL
def local_example():
    local_x = 'This is local'
    print(local_x)


# ENCLOSING - ф-ия возвпащает ф-ию
def enclosing():
    x = 'Enclosing level'  # несмотря на shadowing вернет Х enclosed, если Х закоментить - будет искать в Global scope, если там тоже нет ничего - в Built In

    def inside():
        print(x)

    inside()


# не используй Built in часто, и оно создается при запуске программы.

# global - позволяет переопределить глобальную переменную изнутри ф-ии:

y = 'глобальная переменная'


def report():
    global y
    y = 'теперь её изменили'
    print(y)


if __name__ == '__main__':
    print(y)
    report()
    print(y)
