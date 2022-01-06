def longest(s: str) -> int:
    output = 0
    temp_set = set()
    for i in range(0, len(s)):
        if s[i] not in temp_set:
            temp_set.add(s[i])
        else:
            if len(temp_set) >= output:
                output = len(temp_set)
            temp_set.clear()
            temp_set.add(s[i])

    return output

print(longest("pwwkew"))