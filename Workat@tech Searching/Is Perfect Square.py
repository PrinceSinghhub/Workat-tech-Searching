import math


class Solution:
    def isPerfectSquare(self, n: int) -> bool:
        p = int(math.sqrt(n))

        if p * p == n:
            return True
        return False




