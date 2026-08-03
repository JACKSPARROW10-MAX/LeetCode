class Solution(object):
    def smallestRepunitDivByK(self, k):
        if k%2==0 or k%5==0:
            return -1
        num=1
        for i in range(k):
            if  num%k==0:
                return len(str(num))
            num=(num*10)+1
           
        
        