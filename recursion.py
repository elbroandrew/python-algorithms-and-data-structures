def sum_to_one(n):
    # base case
    if n == 1:
        return n

    print(f'Recursing with input: {n}')
    return sum_to_one(n - 1) + n


print(sum_to_one(7))


# factorial
def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)


print(factorial(12))


# flatten a list
def flatten(my_list):
    result = []
    for element in my_list:
        if isinstance(element, list):
            flat_list = flatten(element)
            result += flat_list
        else:
            result.append(element)

    print(result)
    return result


planets = ['mercury', 'venus', ['earth'], 'mars', [['jupiter', 'saturn']], 'uranus', ['neptune', 'pluto']]
flatten(planets)

# fibonacci
# recursively Big O == 2^N
'''
Стоит отметить, что тут задача сводится либо к выводу последовательности, либо к выводу только числа.
Поэтому алоритм с итерацией можно упростить, убрав массив:

def iterative_fib_short(n):
    a = b = 1
    for i in range(3, n+1):
        c = a + b
        a = b
        b = c

    return b

print(iterative_fib_short(7))

'''


# iterative solution
def iterative_fib(n):
    result = [0, 1]
    for i in range(2, n + 1):
        prev1 = result[i - 1]
        prev2 = result[i - 2]
        result.append(prev1 + prev2)
    print(result)
    return result[n]


iterative_fib(7)


# recursively
def recursive_fib(n):
    # base case
    if n < 2:
        return n

    return recursive_fib(n - 2) + recursive_fib(n - 1)


end = 7
for k in range(0, end + 1):
    print(recursive_fib(k))
