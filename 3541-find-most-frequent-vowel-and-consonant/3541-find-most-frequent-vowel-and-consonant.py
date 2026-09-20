class Solution(object):
    def maxFreqSum(self, s):
        vow=[]
        con=[]
        for i in s:
            if i in "aeiou":
                vow.append(s.count(i))
            else:
                con.append(s.count(i))
        if len(vow)<1:
            a=0
        else:
            a=max(vow)
        if len(con)<1:
            b=0
        else:
            b=max(con)
        return a+b
        