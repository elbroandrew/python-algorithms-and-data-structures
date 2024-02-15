import sys

try:
    import mymodule
except Exception as e:
    print(e)
    import sys
    print("exit")