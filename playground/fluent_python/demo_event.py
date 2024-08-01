
from threading import Thread, Event
import time

def spin():
    time.sleep(3)


def supervisor():
    done = Event()  
    spinner = Thread(target=spin)
    print(f'spinner thread: {spinner.name}')
    spinner.start()
    # done.set()  
    spinner.join()
    return

def main() -> None:
    supervisor()
    print('Done main func.')
    
if __name__ == "__main__":
    main()