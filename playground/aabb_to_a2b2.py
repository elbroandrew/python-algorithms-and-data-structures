from collections import Counter

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

    res_str = ''
    c = Counter(data)
    d = c.most_common()
    
    res_str = ''.join([str(v) for k in d for v in k])
    

    return res_str 

print(shorten_string('a'))
    
# 'a a a b b c d d d'
# 'a a' 

if __name__ == "__main__":
    pass


    

