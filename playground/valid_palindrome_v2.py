

def isPalindrome(s: str) -> bool:

    skips = ".,/ ;:_-+!?"
    s = ''.join([x for x in s if x not in skips]).lower()

    middle = len(s) // 2

    if len(s) % 2 == 0:
        p1 = s[:middle]
    else:
        p1 = s[:middle + 1]

    p2 = s[middle:]

    return p1[::-1] == p2



if __name__ == '__main__':
    test1 = "A man, a plan, a canal: Panama"
    test2 = " "

    assert isPalindrome(test1) == True
    assert isPalindrome(test2) == True