
# recursive solution
def sum_of_digits(n):
    if n < 10:
        return n
    else:
        last_digit = n % 10
        return last_digit + sum_of_digits(n // 10)


x = sum_of_digits(125)
print(x)

# another recursive solution
def sum_digits(n):
    reminder = n % 10
    prime = n // 10
    # base case
    if prime == 0:
        return reminder
        
    return reminder + sum_digits(prime)