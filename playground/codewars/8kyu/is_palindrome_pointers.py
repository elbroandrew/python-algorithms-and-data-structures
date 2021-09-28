def is_pal(s):
    # declare pointers an end and start
    string = s.replace(" ", "").lower()

    p1 = 0
    p2 = len(string) - 1

    while p1 < p2:
        # compare values
        if string[p1] == string[p2]:
            p1 += 1
            p2 -= 1
            continue
        else:
            return False

    return True

if __name__ == '__main__':
    print(is_pal("heh"))
    print(is_pal("heh "))
    print(is_pal("heH"))
    print(is_pal("heH heh"))
    print(is_pal("hello"))
