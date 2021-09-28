def is_palindrome(s):
    # remove whitespaces at beginning and end, or simply TRIM, and remove Capitals

    s = s.strip().lower().replace(" ", "")
    return s == s[::-1]


if __name__ == '__main__':
    print(is_palindrome("hello"))
    print(is_palindrome("heh"))
    print(is_palindrome("heh "))
    print(is_palindrome("Heh"))
    print(is_palindrome("he H "))
