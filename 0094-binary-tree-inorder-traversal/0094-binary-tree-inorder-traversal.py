# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        ans=[]
        self.inord(root,ans)
        return ans
    def inord(self,root,ans):
            if root is None:
                return
            self.inord(root.left,ans)
            ans.append(root.val)
            self.inord(root.right,ans)

