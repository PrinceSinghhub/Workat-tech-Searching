class Solution:
    def calculateMedianOfMatrix(self, matrix: List[List[int]]) -> int:
        ans = []

        for i in matrix:
            ans += i
        ans.sort()
        mid = len(ans) // 2
        return ans[mid]



