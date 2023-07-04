
def is_palindrome(s: str) -> bool:

    s = s.lower()
    new_line = [x for x in s if x.isalnum()]
    print(new_line)
    p1 = 0
    p2 = len(new_line) - 1

    while p1 < p2:
        if new_line[p1] == new_line[p2]:
            p1 += 1
            p2 -= 1
        else:
            return False
    return True




if __name__ == '__main__':
    test1 = "A man, a plan, a canal: Panama"
    test2 = " "

    assert is_palindrome(test1) == True
    assert is_palindrome(test2) == True
