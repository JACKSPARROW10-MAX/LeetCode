class Solution(object):
    def digitFrequencyScore(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans=[]
        for i in set(str(n)):
            ans.append(int(i)*str(n).count(str(i)))
        return sum(ans)