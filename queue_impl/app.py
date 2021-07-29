from queue import Queue

cars = Queue()

cars.add('Honda')
cars.add('Toyota')
cars.add('Nissan')

cars.pop()

print(cars.show_all())
