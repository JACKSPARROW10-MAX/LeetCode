class Solution(object):
    def replaceDigits(self, s):
        ch=[]
        num=[]
        for i in s:
            if i in "0123456789":
                num.append(i)
            else:
                ch.append(i)
        ans=""
        for i in range(len(num)):
            ans+=ch[i]
            ans+=chr(ord(ch[i])+int(num[i]))
        if len(ch)>len(num):
            ans+=ch[-1]
        return ans
