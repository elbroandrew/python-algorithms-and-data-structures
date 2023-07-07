import gevent
from gevent import Greenlet
import gevent.queue


queue = gevent.queue.Queue()
queue.put("hello")

def foo():
    print("FOO START")
    gevent.sleep(0)  # sleep(0) similar to yield, слип возвращает контроль.
    print("FOO END")


def bar():
    print("BAR START")
    print(gevent.get_hub())
    gevent.sleep(1)
    print(queue.get())
    print("BAR END")


print(gevent.get_hub())


# Greenlet.spawn is the same as gevent.spawn

t1 = Greenlet.spawn(foo)  # same as: g = Greenlet(foo, *args); g.start()
t2 = gevent.spawn(bar)
t3 = gevent.spawn(lambda x: x + 2, 10)
# print(gevent.get_hub(t1)) # returns event loop thread

print(t2.started)  # state of a greenlet
threads = [t1,t2, t3]


gevent.joinall(threads)
print(t3.value)  # get 12 from lambda