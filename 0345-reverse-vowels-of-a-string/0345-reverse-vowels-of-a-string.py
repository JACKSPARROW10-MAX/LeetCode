class Solution(object):
    def reverseVowels(self, s):
        v=[]
        c=[]
        for i in s:
            if i in "aeiouAEIOU":
                v.append(i)
            else:
                c.append(i)
        v=v[::-1]
        ans=""
        p=0
        q=0
        for i in s:
            if i in "aeiouAEIOU":
                ans+=v[p]
                p+=1
            else:
                ans+=c[q]
                q+=1
        return ans

        