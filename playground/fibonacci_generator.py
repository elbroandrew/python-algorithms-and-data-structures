

def gen():
    a, b =  0, 1

    while True:
        yield a
        a += b
        yield b
        b += a


def main(x: int):
    g = gen()
    for i in range(x):
        res = next(g)
        print(res)

if __name__ == '__main__':
    main(10)