class Solution(object):
    def findErrorNums(self, nums):
        temp=0
        mx=max(nums)
        for i in nums:
             if nums.count(i)>=2:
                temp=i
        exp=(len(nums)*(len(nums)+1))//2
        act=sum(nums)
        ans=exp-act+temp
        return[temp,ans]