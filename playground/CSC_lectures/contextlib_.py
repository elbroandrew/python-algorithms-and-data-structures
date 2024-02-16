import io
from contextlib import redirect_stdout



file = io.StringIO()
with redirect_stdout(file):
    print("hello")
    
print(file.getvalue())





