# recursively

def findElement(arr, value):
    # base case
    if len(arr) <= 0:
        print("length 0, not found")
        return False
    if arr.pop() == value:
        print("Found")
        return True
    else:
        return findElement(arr, value)


def main():
    findElement(['t', 'e', 's', 't'], 'e')


if __name__ == '__main__':
    main()
