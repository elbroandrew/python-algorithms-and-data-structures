import time

for i in range(5):
    print(f'\r{i}', end="", flush=True)
    time.sleep(0.5)
    
print("\rEND")