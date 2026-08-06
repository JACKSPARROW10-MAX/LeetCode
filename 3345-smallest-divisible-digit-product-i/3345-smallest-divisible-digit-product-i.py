class Solution(object):
    def smallestNumber(self, n, t):
       while(n):
        num=str(n)
        pro=1
        for i in num:
            pro*=int(i)
        if pro%t==0:
            return n
        else:
            n=n+1
         
        