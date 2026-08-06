class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        temp=[]
        for i in range(len(boxes)):
            if boxes[i]=="1":
                temp.append(i)
        ans=[]
        for i in range(len(boxes)):
            sm=0
            for j in temp:
                sm+=abs(i-j)
            ans.append(sm)
        return ans