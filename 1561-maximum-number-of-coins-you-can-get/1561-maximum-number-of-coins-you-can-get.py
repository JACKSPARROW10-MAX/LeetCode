class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        n=len(piles)//3
        ans=0
        piles=piles[n:]
        i=0
        while(i<len(piles)):
            ans+=piles[i]
            i+=2
            
        return ans