# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        for i in range(1, m):
            cur = cur.next
            
        tail = cur.next
        for i in range(m, n):
            if tail is None:
                break
            tmp = tail.next
            tail.next = tmp.next
            tmp.next = cur.next
            cur.next = tmp
            
        return dummy.next