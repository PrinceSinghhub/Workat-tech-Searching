class Solution:
    def getInsertPosition(self, arr: List[int], key: int) -> int:
        # add your logic here

        if max(arr) <= key:
            return len(arr)

        for i in arr:
            if i >= key:
                return arr.index(i)





