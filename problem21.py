# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ptr1, ptr2 = l1, l2
        ptr = ListNode(0)
        head = ptr
        while ptr1 is not None and ptr2 is not None:
            if ptr1.val <= ptr2.val:
                ptr.next = ptr1
                ptr1 = ptr1.next
            else:
                ptr.next = ptr2
                ptr2 = ptr2.next
            ptr = ptr.next
        if ptr1 is None:
            ptr.next = ptr2
        else:
            ptr.next = ptr1
        return head.next