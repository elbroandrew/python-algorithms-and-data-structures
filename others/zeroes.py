# number of zeroes

def get_zeroes(n: int) -> int:
    if n == 0: return 1

    result = 0
    while(n % 10 == 0):
        result += 1
        n //= 10

    return result

if __name__ == '__main__':

    cases = [0, 1, 10, 22, 100]
    answers = [1, 0, 1, 0, 2]

    for number, output in zip(cases, answers):
        assert get_zeroes(number) == output

    print("Done.")


