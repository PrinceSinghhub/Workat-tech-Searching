from collections import Counter


class Solution:
    def findNonRepeatingElement(self, arr: List[int]) -> int:

        myd = Counter(arr)

        for key, val in myd.items():
            if val == 1:
                return key
        return -1

