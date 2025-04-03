# using sliding window approach 
# initialise l,r ptrs 
# keep track of cur_sum,min_len,length
# iterate through the array  
# compute the cur_sum and increment r ptr
# iterate until condition is satisified cur_sum >= target, return min(min_length,length)
# we shrink the sliding window, increment l ptr and reduce nums[l] from curr_sum 
# Edge case if curr_sum != target return 0  

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        cur_sum = 0
        min_length = float('inf')
        
        for r in range(len(nums)):
            cur_sum += nums[r]
            
            # Shrink window while it satisfies the condition
            while cur_sum >= target:
                min_length = min(min_length, r - l + 1)
                cur_sum -= nums[l]
                l += 1

        return 0 if min_length == float('inf') else min_length
