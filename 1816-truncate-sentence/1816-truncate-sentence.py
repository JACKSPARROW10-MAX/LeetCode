class Solution(object):
    def truncateSentence(self, s, k):
        ans=s.split()
        res=""
        for i in range(k):
            res+="".join(ans[i])+" "
        res=res[:-1]
        return res
           
        