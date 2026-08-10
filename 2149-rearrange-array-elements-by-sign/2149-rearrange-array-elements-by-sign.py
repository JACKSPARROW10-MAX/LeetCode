class Solution(object):
    def rearrangeArray(self, nums):
        pos=[]
        neg=[]
        for i in nums:
            if i<0:
                neg.append(i)
            else:
                pos.append(i)
        ans=[]
        for i in range(len(neg)):
            ans.append(pos[i])
            ans.append(neg[i])
        return ans