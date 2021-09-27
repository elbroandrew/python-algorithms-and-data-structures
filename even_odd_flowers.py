"""
два цветка,
лепестки нечетные у одного и лепестки четные у другого дают любовь.
"""


def main():
    print(lovefunc(1, 4))
    print(lovefunc(2, 2))
    print(lovefunc(0, 1))
    print(lovefunc(0, 0))


def lovefunc(flower1: int, flower2: int) -> bool:
    return (flower1 - flower2) % 2 == 0


if __name__ == '__main__':
    main()
