class Solution(object):
    def maxProduct(self, nums):
       nums.sort()
       a=nums[-1]-1
       b=nums[-2]-1
       return a*b