class Solution(object):
    def maxSubArray(self, nums):
        maxsum=nums[0]
        cursum=0
        
        for i in range(len(nums)):
            if cursum+nums[i]<nums[i]:
                cursum=nums[i]
            else :
                cursum+=nums[i]
            if maxsum<cursum:
                maxsum=cursum 
        return maxsum