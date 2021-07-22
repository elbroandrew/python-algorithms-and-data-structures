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
