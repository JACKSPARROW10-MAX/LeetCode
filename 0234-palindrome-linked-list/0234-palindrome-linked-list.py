# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
       temp = head
       ans=[]
       while(temp!=None):
           ans.append(temp.val)
           temp=temp.next
       if ans==ans[::-1]:
           return True
       return False
        