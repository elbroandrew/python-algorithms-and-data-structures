def sum_of_numbers(*params):
    result = 0
    for num in params:
        result += num

    return result


x = sum_of_numbers(1,2,3,4,5)
print(x)