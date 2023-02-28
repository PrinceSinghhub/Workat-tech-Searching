# here contains some dublicates slement find the first ans last occurence of element/index using Binary Serach
class Solution:

    def findIndex(self, arr, x, boll):

        start = 0
        end = len(arr) - 1

        ans = -1

        while start <= end:
            mid = start + (end - start) // 2

            if x > arr[mid]:
                start = mid + 1

            if x < arr[mid]:
                end = mid - 1

            if x == arr[mid]:

                ans = mid
                if boll == True:
                    end = mid - 1

                else:
                    start = mid + 1
        return ans

    def searchRange(self, arr, x):
        ans = [-1, -1]

        first = self.findIndex(arr, x, True)
        last = self.findIndex(arr, x, False)

        ans[0] = first
        ans[1] = last

        return ans





