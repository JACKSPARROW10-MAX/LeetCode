class Solution(object):
    def recoverOrder(self, order, friends):
       ans=[]
       for i in order:
          if i in friends:
             ans.append(i)
       return ans