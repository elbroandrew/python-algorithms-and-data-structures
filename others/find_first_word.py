""" find the first word of a string"""


# slow solution

def find_word(s: str) -> str:
    return s.split(' ')[0]


def main():
    strings = [
        "hello world",
        "hi"
    ]

    answers = [
        "hello",
        "hi"
    ]

    for string, answer in zip(strings, answers):
        print(f"{find_word(string)} == {answer}")
        assert find_word(string) == answer


# better solution


if __name__ == '__main__':
    main()
