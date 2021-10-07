from stack import Stack

""" 
необходимо определить сбалансированную последовательность и вернуть true, а именно:
'()[{([]())}]' true
'[{]}' false
'(()' false
'}{' false
"" true - пустая строка

"""


def is_open(char: str) -> bool:
    return char == '{' or char == '[' or char == "("


def is_pair(opened: str, closed: str) -> bool:
    return opened == '{' and closed == '}' or opened == '(' and closed == ')' or opened == '[' and closed == ']'


def is_balanced(s: str) -> bool:
    st = Stack()

    for i in range(0, len(s)):
        if is_open(s[i]):
            st.push(s[i])
        else:
            if not st.is_empty() and is_pair(st.top(), s[i]):
                st.pop()
            else:
                return False

    return st.is_empty()


def main():

    entries = ['()[{([]())}]',
               '[{]}',
               '(()',
               '}{',
               ""]

    for entry in entries:
        print(is_balanced(entry))


if __name__ == '__main__':
    main()
