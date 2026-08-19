class Solution(object):
    def minElement(self, nums):
        ans=[]
        for i in nums:
            b=self.digit(i)
            ans.append(b)
        return min(ans)
    def digit(self,n):
        a=str(n)
        sm=0
        for i in a:
            sm+=int(i)
        return sm
        