# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ptr1, ptr2, ptrResult = l1, l2, ListNode(0)
        headNode = ptrResult
        tmp = 0
        while ptr1 is not None and ptr2 is not None:
            ptrResult.next = ListNode(0)
            ptrResult = ptrResult.next
            tmp = ptr1.val + ptr2.val + tmp
            ptrResult.val = tmp % 10
            tmp /= 10
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        if ptr1 is not None:
            ptr = ptr1
        elif ptr2 is not None:
            ptr = ptr2
        elif tmp>0:
            ptr = ListNode(0)
        else:
            return headNode.next
        ptrResult.next = ptr
        tmp += ptr.val
        ptr.val = tmp%10
        while tmp >= 10:
            tmp /= 10
            if ptr.next is None:
                ptr.next = ListNode(0)
            ptr = ptr.next
            tmp += ptr.val
            ptr.val = tmp % 10
        return headNode.next

