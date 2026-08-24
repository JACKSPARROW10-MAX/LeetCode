class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        ans=[]
        m=max(candies)
        for i in candies:
            if i+extraCandies>=m:
                ans.append(True)
            else:
                ans.append(False)
        return ans

        