def factorial(n):
    if n <= 0:
        return ValueError('Число должно быть больше нуля.')
    if n <= 1:
        return 1
    return n * factorial(n - 1)


print(factorial(0))