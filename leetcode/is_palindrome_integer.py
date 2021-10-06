class Solution:
    """ -121 is false """
    # trivial solution with string
    @staticmethod
    def isPal_1(x: int) -> bool:
        return str(x) == str(x)[::-1]

    # without string
    @staticmethod
    def isPal_2(x: int) -> bool:
        y = x
        s = 0
        while x > 0:
            s *= 10
            s += x % 10
            x //= 10
        return y == s


if __name__ == '__main__':
    s1 = Solution.isPal_1(-121)
    print(s1)

    s2 = Solution.isPal_2(-121)
    print(s2)
