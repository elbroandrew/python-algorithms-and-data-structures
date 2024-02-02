from collections import deque

# deque вставляет в начало очень быстро,  отличие от списка

q = deque(iterable=[1,2,3,4,5,6,7])
q.appendleft(100)
print(q)

q2 = deque([1,2,3,4], maxlen=3)
print(q2) # 2,3,4

# use maxlen with file to print last 2 strings -- similar to unix "tail" command:

with open("points.csv") as file:
    a_deque = deque(file, maxlen=2)

for line in a_deque:
    print(line.rstrip())  # remove '\n'

# дека - потокобезопасна, можно использовать в многопоточных приложениях, например pub/sub паттерн.




