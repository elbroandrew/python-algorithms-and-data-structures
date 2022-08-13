from deques_example import MyDeque

my_deque = MyDeque()

my_deque.push_back(5)
print(my_deque.is_empty())
my_deque.pop_back()
my_deque.pop_back()

my_deque.show()