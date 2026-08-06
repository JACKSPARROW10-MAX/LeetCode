class Solution(object):
    def numberOfBeams(self, bank):
        temp=[]
        for i in bank:
            p=i.count("1")
            if p!=0:
                temp.append(p)
        if len(temp)<2:
            return 0
        ans=0
        for i in range(len(temp)-1):
            ans+=temp[i]*temp[i+1]
        return ans
        
        