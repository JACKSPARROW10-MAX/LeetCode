class Solution(object):
    def firstUniqChar(self, s):
        temp={}
        for i in s:
            if i in temp:
                temp[i]+=1
            else:
                temp[i]=1
        print(temp)
        for i in s:
            if temp[i]==1:
                return s.index(i)
        return -1
        