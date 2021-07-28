'''замыкание'''

def f(y):
    x = 5
    def mul():
        return x * y
    
    return mul


if __name__ == '__main__':
    result = f(5)()
    print(result)

