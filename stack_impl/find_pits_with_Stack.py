import pytest

"""
некий уровень моря имеется,
получаем диаграмму, где надо определить впадины.
'UD' - up, down -- это не впадина, а пик.
'DU' - down, up - это впадина.
'UUDDDU' - здесь одна впадина.
'UDDDUDUUU' - тоже одна впадина
'DUDUUUDDDDUDU' - 3 впадины
"""
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        if len(self.items) == 0:
            return None
        return self.items[len(self.items) - 1]

    def get_size(self):
        return len(self.items)

    def is_empty(self) -> bool:
        return len(self.items) == 0


def is_pair(first: str, second: str) -> bool:
    return first == 'U' and second == 'D' or first == 'D' and second == 'U'


def count_pits(val: str):
    total_pits: int = 0
    st = Stack()

    d = {
        'U': 1,
        'D': -1
    }

    prev = 0

    for i in range(len(val)):
        if not st.is_empty():
            if is_pair(st.top(), val[i]):
                st.pop()
            else:
                st.push(val[i])
        else:
            st.push(val[i])
            prev = d[val[i]]

        if prev < 0:
            if d[st.top()] < 0 or st.is_empty():
                total_pits += 1
                prev = 0

    return total_pits

entries = [('UD', 0),
           ('DU', 1),
           ('UUDDDU', 1),
           ('DUDUUUDDDDUDU', 3)
           ]

@pytest.mark.parametrize('a, b', entries)
def test_pits_counter(a, b):
    for _ in entries:
        assert count_pits(a) == b


def main():
    s = "DDDUUU" # 1 pit
    print(count_pits(s))


if __name__ == '__main__':
    main()
