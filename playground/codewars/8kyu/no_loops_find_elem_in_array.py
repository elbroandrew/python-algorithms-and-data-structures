# recursively

def findElement(arr: list, value) -> bool:
    # base case
    if len(arr) <= 0:
        print("length 0, not found")
        return False
    if arr.pop() == value:
        print("Found")
        return True
    else:
        findElement(arr, value)


def main():
    findElement([1,2,5,3,7,4], 0)


if __name__ == '__main__':
    main()
