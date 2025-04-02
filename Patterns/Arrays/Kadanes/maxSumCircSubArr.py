class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cur_max_sum,cur_min_sum = 0,0 
        max_sum = nums[0]
        min_sum = nums[0] 
        total_sum = 0 
        for i in range(len(nums)):
            total_sum += nums[i]
            
            if cur_max_sum < 0:
                cur_max_sum = 0 
            cur_max_sum += nums[i]
            max_sum = max(max_sum,cur_max_sum)

            if cur_min_sum > 0:
                cur_min_sum = 0 
            cur_min_sum += nums[i]
            min_sum = min(min_sum,cur_min_sum)

        # Edge case if all nos are minimum
      
        if max_sum < 0:
            return max_sum 
        return max(max_sum,total_sum - min_sum)
