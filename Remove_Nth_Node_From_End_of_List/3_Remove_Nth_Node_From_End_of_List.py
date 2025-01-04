# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        slow = head
        fast = head

        # Pindahkan pointer fast sejauh n langkah
        for _ in range(n):
            fast = fast.next
        
        # Jika fast mencapai akhir (menghapus elemen pertama)
        if not fast:
            return head.next
        
        # Pindahkan slow dan fast hingga fast mencapai node terakhir
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        # Hapus node ke-n dari akhir
        slow.next = slow.next.next

        return head
