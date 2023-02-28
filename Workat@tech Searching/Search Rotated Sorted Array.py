class Solution:
    def getElementIndex(self, array: List[int], target: int) -> int:
        if target in array:
            return array.index(target)
        return -1



