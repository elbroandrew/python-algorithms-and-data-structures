import sys
import traceback

try:
    import mymodule
except Exception as e:
    print(e.with_traceback(e.__traceback__))
    import sys
    traceback.print_tb(e.__traceback__)