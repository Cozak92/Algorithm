# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def sortedListToBST(self, head):
            if not head:
                return 
            if not head.next:
                return TreeNode(head.val)
            # here we get the middle point,
            # even case, like '1234', slow points to '2',
            # '3' is root, '12' belongs to left, '4' is right
            # odd case, like '12345', slow points to '2', '12'
            # belongs to left, '3' is root, '45' belongs to right
            slow, fast = head, head.next.next
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            # tmp points to root
            tmp = slow.next
            # cut down the left child
            slow.next = None
            root = TreeNode(tmp.val)
            root.left = self.sortedListToBST(head)
            root.right = self.sortedListToBST(tmp.next)
            return root
        return sortedListToBST(self,head)