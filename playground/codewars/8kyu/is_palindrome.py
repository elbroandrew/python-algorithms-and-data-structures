def is_palindrome(s):
    """
     remove whitespaces replace()
     remove Capitals lower()

    """

    s = s.lower().replace(" ", "")
    return s == s[::-1]


if __name__ == '__main__':
    print(is_palindrome("hello"))
    print(is_palindrome("heh"))
    print(is_palindrome("heh "))
    print(is_palindrome("Heh"))
    print(is_palindrome("he H "))
