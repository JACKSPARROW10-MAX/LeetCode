class Solution:
    def sortVowels(self, s: str) -> str:
        vow=[]
        for i in s:
            if i in "aeiouAEIOU":
                vow.append(i)
        vow.sort()
        p=0
        ans=""
        for i in range(len(s)):
            if s[i] in "aeiouAEIOU":
               s=s[:i]+vow[p]+s[i+1:]
               p+=1
        return s