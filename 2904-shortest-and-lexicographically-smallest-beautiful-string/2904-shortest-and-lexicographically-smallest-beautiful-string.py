class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        i=0
        j=i+k
        ans=[]
        if s.count("1")<k:
            return ""
        while(j<=len(s)):
            a=s[i:j]
            if a.count("1")==k:
                ans.append(a)
            if j == len(s):
                i += 1
                j = i + k
            else:
                j += 1
        print(ans)
        ans.sort()
        minimum = min(len(x) for x in ans)
        for i in ans:
            if len(i)==minimum:
                return i
        