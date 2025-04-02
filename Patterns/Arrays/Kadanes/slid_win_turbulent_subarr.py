# Kadanes/Sliding window algo 
#  use 2 ptrs l,r
#  keep track of the sign 
#  compare curr and prev and check the sign
#  Similarly compare curr and next and check sign
#  if elements are equal update left ptr
# Note: Implementing for loop is a bit tricky the edge case arr[r] == arr[r - 1] will get messy
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l, r, res, prev = 0, 1, 1, ""

        while r < len(arr):
            if arr[r - 1] > arr[r] and prev != ">":
                res = max(res, r - l + 1)
                r += 1
                prev = ">"
            elif arr[r - 1] < arr[r] and prev != "<":
                res = max(res, r - l + 1)
                r += 1
                prev = "<"
            else:
                r = r + 1 if arr[r] == arr[r - 1] else r
                l = r - 1
                prev = ""

        return res
