class Solution:
    def getNegativeNumbersCount(self, arr: List[int]) -> int:

        count = 0
        for i in arr:
            if i < 0:
                count += 1
        return count



