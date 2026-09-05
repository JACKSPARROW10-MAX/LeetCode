class Solution(object):
    def firstStableIndex(self, nums, k):
        n=len(nums)
        premx=[0]*n
        premx[0]=nums[0]
        for i in range(1,n):
           premx[i]=max(premx[i-1],nums[i])

        sufmn=[0]*n
        sufmn[n-1]=nums[n-1]
        for i in range(n-2,-1,-1):
            sufmn[i]=min(sufmn[i+1],nums[i])

        for i in range(n):
            if premx[i]-sufmn[i]<=k:
                return i

        return -1
        