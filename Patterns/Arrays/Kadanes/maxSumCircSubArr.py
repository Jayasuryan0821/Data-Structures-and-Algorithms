# For this soln 
# we have to find the max sum and min sum in circ sub array 
# also compute the total 
# ans is max(max_sum,total - min_circ_sub_sum)
# ex, nums =  [5,-3,5]
# Since this is circular subarray where it will be:
#  ........->5->5->3->5->5->3->5->..........
# iterate through the array 
# max_circ_sub_arr_sum = 7
# min_circ_sub_arr_sum = -3 
# total = 5 + 5 + -3 = 7 
# ans = max(7,7 -(-3)) = 10 
#  edge case if all elements are negative [-3,-2,-3] return the max_sum

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cur_max_sum,cur_min_sum,total = 0,0,0
        min_sum,max_sum = nums[0],nums[0]

        for i in range(len(nums)):
            total += nums[i]
            if cur_max_sum < 0:
                cur_max_sum = 0 
            
            cur_max_sum += nums[i]
            
            max_sum = max(max_sum,cur_max_sum)

            if cur_min_sum > 0:
                cur_min_sum = 0 
            cur_min_sum += nums[i]
            min_sum = min(min_sum,cur_min_sum)

        if max_sum < 0:
            return max_sum
        return max(max_sum,total - min_sum) 
