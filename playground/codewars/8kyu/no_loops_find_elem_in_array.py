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


# best solution
def check(my_list, x):
    return x in my_list


def main():
    findElement(['t', 'e', 's', 't'], 'e')
    print(check(['t', 'e', 's', 't'], 'e'))


if __name__ == '__main__':
    main()
