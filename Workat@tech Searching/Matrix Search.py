class Solution:
    def searchMatrix(self, matrix: List[List[int]], key: int) -> bool:
        # add your logic here

        for i in matrix:
            if key in i:
                return True
        return False



