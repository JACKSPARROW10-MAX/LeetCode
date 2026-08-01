class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        a="Push"
        b="Pop"
        ans=[]
        temp=[]
        for i in range(1,n+1):
            ans.append(a)
            if i not in target:
                ans.append(b)
            else:
                temp.append(i)
            if temp==target:
                break
        return ans

