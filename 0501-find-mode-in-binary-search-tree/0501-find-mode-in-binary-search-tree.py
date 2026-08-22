# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def findMode(self, root):
        ans=[]
        self.inorder(root,ans)
        count=Counter(ans)
        mx_freq=max(count.values())
        return [num for num,freq in count.items() if freq==mx_freq]
        
    
    def inorder(self,root,ans):
        if root is None:
            return
        self.inorder(root.left,ans)
        ans.append(root.val)
        self.inorder(root.right,ans)


        
        