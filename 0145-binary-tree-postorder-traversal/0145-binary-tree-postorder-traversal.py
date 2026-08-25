# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
       ans=[]
       self.post(root,ans)
       return ans
    def post(self,root,ans):
        if root is None:
            return
        self.post(root.left,ans)
        self.post(root.right,ans)
        ans.append(root.val)
        