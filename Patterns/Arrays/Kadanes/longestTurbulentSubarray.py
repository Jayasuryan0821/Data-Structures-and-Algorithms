# Brute force approach 
# 2 for loops 
# compare the first 2 elements in array and check the signs if they are equal we skip them 
# we compare the next pair of elements and similarly check the signs if they are equal break out of loop, otherwise we can update the signs 


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        max_len = 1 

        for i in range(len(arr) - 1):
            
            if arr[i] == arr[i + 1]:
                continue 
            
            sign = 1 if arr[i] > arr[i + 1] else 0 
            end = i + 1

            for j in range(i + 1,len(arr) - 1):
                if arr[j] == arr[j + 1]:
                    break 
                
                cur_sign = 1 if arr[j] > arr[j + 1] else 0 
                
                if sign == cur_sign:
                    break
            
                sign = cur_sign 
                end = j + 1
            max_len = max(max_len,end - i + 1)
        return max_len
