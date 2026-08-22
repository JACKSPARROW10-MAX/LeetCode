class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        a=str(n)
        sm=0
        ml=1
        for i in a:
            sm+=int(i)
            ml*=int(i)
        if n%(sm+ml)==0:
            return True
        return False
        