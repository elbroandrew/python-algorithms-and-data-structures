""" чтоб выдавало '21.00', '5.35' """


def usdcny(usd):
    return f"{round(usd * 6.75, 2)} Chinese Yuan"


def main():
    print(usdcny(1))


if __name__ == '__main__':
    main()
