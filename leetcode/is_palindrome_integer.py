class Solution:

    # trivial solution with string
    @staticmethod
    def isPal_1(x: int) -> bool:
        return str(x) == str(x)[::-1]


if __name__ == '__main__':
    y = Solution.isPal_1(-121)
    print(y)
