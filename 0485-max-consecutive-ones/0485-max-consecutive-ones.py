class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        temp=[]
        p=0
        if p not in nums:
            return len(nums)
        if len(nums)<2 and nums[0]==1:
            return 1
        if len(nums)<2 and nums[0]==0:
            return 0
        for i in range(len(nums)):
            if nums[i]==0:
                temp.append(i)
        mx=temp[0]
        mx=max(mx,len(nums)-temp[-1]-1)
        for i in range(len(temp)-1):
            diff=temp[i+1]-temp[i]-1
            mx=max(mx,diff)
        return mx
            

        