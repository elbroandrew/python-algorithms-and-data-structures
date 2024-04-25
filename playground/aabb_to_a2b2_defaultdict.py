from collections import defaultdict

def shorten_string(data: str):
    
    data = data.strip()
    
    length = len(data)
    
    try:
        if type(data) != str:
            raise AttributeError("Data must be a valid string.")
    
        if length == 0:
            raise AttributeError("Data must not be empty string.")
    except AttributeError:
        print(f"ERROR")
    
    if length == 1:
        return f'{data[0]}1'

    
    
    o = defaultdict(int)
    
    for ch in data:
        o[ch] += 1
    
    print(o)
    

    return ''.join([f"{k}{v}" for k,v in o.items()])

shorten_string("aab")
    

if __name__ == "__main__":
    print(shorten_string('aab'))


    

