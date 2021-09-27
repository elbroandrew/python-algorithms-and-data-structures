""" чтоб выдавало '21.00', '5.35' """


def usdcny(usd):
    return f"{(usd * 6.75):.2f} Chinese Yuan"

"""
or
def usdcny(usd):
    return "{:.2f} Chinese Yuan".format(usd * 6.74)
"""

def main():
    print(usdcny(1))


if __name__ == '__main__':
    main()
