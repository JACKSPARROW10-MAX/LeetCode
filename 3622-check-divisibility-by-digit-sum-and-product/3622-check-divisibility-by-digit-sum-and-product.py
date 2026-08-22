class Solution(object):
    def checkDivisibility(self, n):
        a=str(n)
        b=0
        c=1
        for i in a:
            b+=int(i)
            c*=int(i)
        if n%(b+c)==0:
            return True
        return False

        