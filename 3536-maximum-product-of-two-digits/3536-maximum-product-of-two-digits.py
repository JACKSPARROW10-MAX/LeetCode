class Solution(object):
    def maxProduct(self, n):
     p=sorted(str(n))
     return int(p[-1])*int(p[-2])

        