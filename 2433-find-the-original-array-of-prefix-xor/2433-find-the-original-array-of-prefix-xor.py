class Solution(object):
    def findArray(self, pref):
        pref=pref[::-1]
        temp=[]
        for i in range(len(pref)-1):
            temp.append(pref[i]^pref[i+1])
        temp.append(pref[-1])
        temp=temp[::-1]
        return temp
        