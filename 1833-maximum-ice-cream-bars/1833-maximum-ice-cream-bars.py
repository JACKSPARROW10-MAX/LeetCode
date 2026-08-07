class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        total=0
        count=0
        costs.sort()
        for i in costs:
            if total+i<=coins:
                total+=i
                count+=1
            else:
                continue
        return count