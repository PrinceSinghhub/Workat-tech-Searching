class Solution:
    def getNextGreaterElement(self, arr: List[int], key: int) -> int:
        ans = []

        for i in arr:
            if i > key:
                ans.append(i)

        if len(ans) == 0:
            return key
        return min(ans)



