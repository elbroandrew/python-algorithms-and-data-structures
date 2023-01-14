
def isPalindrome(s: str) -> bool:

    skips = ".,/ ;:_-+!?"
    new_line = ''.join([x for x in s if x not in skips]).lower()
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

    assert isPalindrome(test1) == True
    assert isPalindrome(test2) == True
