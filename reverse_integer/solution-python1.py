class Solution:
    def reverse(self, x: int) -> int:
        multiplier = 1

        if x < 0:
            x = -x
            multiplier = -1

        """
        Interesting that modulo with negative numbers
        yields a different result in Python than it does in C, i.e.
        (-5) % 4 = (-2 × 4 + 3) % 4 = 3

        learn more at: https://julianpark.me/posts/python-modulo
        """
        reverted = x % 10
        x = x // 10

        while x != 0:
            # check is not necessary in Python 3, as it switches to long when
            # the limit is exceeded, int.maxsize no longer exists in Python 3
            if reverted * 10 + x % 10 >= 2147483647:
                return 0

            # move all digits to the right and add a new digit
            reverted = reverted * 10 + x % 10

            x = x // 10

        return reverted * multiplier
