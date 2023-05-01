"""
создаёт объекты
"""


class Factory:

    def create_product(self):
        return Product()


class Product:
    pass


def main():
    factory: Factory = Factory()
    product: Product = factory.create_product()


if __name__ == '__main__':
    main()
