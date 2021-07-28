from stack import Stack

cars = Stack()

cars.push('Mazda')
cars.push('Honda')
cars.push('Toyota')

print(cars.items)

print(cars.next_to_remove())

print(cars.pop())

print(cars.items)

print(cars.next_to_remove())

print(cars.push('Nissan'))

print(cars.items)

print(cars.next_to_remove())

