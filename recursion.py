def sum_to_one(n):
    # base case
    if n == 1:
        return n

    print(f'Recursing with input: {n}')
    return sum_to_one(n - 1) + n


print(sum_to_one(7))
