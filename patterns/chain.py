"""
по цепочке добавляется функционал
"""
class A:

    def print_sth:
        print("A")

class B:

    def method_b(self):
        print("B") # here goes instance B logic
        a = A()
        a.print_sth()

class C:

    def method_c(self):
        # logic for C
        print("C")
        b = B()
        b.method_b()

# and so on

def main():
    chain = C()
    c.method_c()

if __name__ == '__main__':
    main()