def main():

    '''в пайтоне нет встроенного unsigned int, только signed'''
    print(~23) # 24 т.к. хранит signed число, с unsigned было бы 4292967272
    print(17 | (1 << 2)) # выставить 3 бит в 1 (результат 21)
    # вернуть в ноль 3 бит
    print(21 & ~(1 << 2)) # результат 17


if __name__ == '__main__':
    main()
