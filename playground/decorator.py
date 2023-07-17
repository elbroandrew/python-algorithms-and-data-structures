"""декоратор связан с замыканием"""

def convertor(f):
    print("converting int to float ...")
    def wrapper(a):
        return float(f(a))
    return wrapper


@convertor
def func(n: int):
    return n*10


g = func(4)
print(g)



# decorator with arguments "просто еще уровень вложенности добавляется"

def repeat(n: int):

    def convertor(f):

        print("converting int to float ...")

        result = []

        def wrapper(a):

            for _ in range(n):

                r = float(f(a))
                result.append(r)

            return result

        return wrapper

    return convertor


@repeat(3)
def func2(n: int):
    return n*10


d = func2(50)
print(d)