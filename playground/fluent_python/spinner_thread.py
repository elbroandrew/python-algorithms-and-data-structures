import itertools
import time
from threading import Thread, Event

# EVENT - это событие, которое слушают ВСЕ треды одновременно. Если в одном треде установлю его в Тру через (event.set() ), то в другом это тоже будет видно.

def spin(msg: str, done: Event) -> None:
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, end='', flush=True)
        if done.wait(.1):  # заставляет данный тред ждать 0.1 сек, пока в мейн треде счетчик 3 сек не пройдет и не установится done.set (в True)Б тем самым можно менять скорость анимации спиннера.
            break
        
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')
    

def slow() -> int:
    time.sleep(3)
    return 42

def supervisor() -> int:
    done = Event()  # event нужен чтобы переключиться на другой тред
    spinner = Thread(target=spin, args=('thinking!', done))
    print(f'spinner object: {spinner}')
    spinner.start()
    result = slow()
    done.set()  # ЗДЕСЬ  и устанавливаю эвент.
    spinner.join()
    return result

def main() -> None:
    result = supervisor()
    print(f'Answer: {result}')
    
if __name__ == "__main__":
    main()