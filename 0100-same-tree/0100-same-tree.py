# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        ans1=[]
        ans2=[]
        self.trav(p,ans1)
        self.trav(q,ans2)
        return ans1==ans2

    def trav(self,a,arr):
        if a is None:
            arr.append(None)
            return
        arr.append(a.val)
        self.trav(a.left,arr)
        self.trav(a.right,arr)        
        