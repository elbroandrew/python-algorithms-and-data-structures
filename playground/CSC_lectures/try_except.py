

with open("mytext.txt") as f:
    text = f.read()
    process(text)  # надо закрыть файл как можно скорее.
    
    
with open("mytext.txt") as f:
    text = f.read()
process(text)  # поэтому лучше сделать вот так, тем более в питоне скопов не с with (или не только с with?)