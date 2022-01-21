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
    # for first solution
    for string, answer in zip(strings, answers):
        print(f"{find_word(string)} == {answer}")
        assert find_word(string) == answer

    # for second solution
    for string, answer in zip(strings, answers):
        print(f"{first_word(string)} == {answer}")
        assert first_word(string) == answer


# better and quicker solution

def first_word(text: str) -> str:
    index: int = text.find(" ")
    return text[:index] if index != -1 else text


# solution 3
def first_word_3(text):
    try:
        index = text.index(" ")
        return text[:index]
    except ValueError:
        return text


if __name__ == '__main__':
    main()
