# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Jika salah satu dari list1 atau list2 kosong, kembalikan list yang tidak kosong
        if not list1 or not list2:
            return list1 if list1 else list2
        
        # Jika nilai di list1 lebih besar dari nilai di list2, tukar list1 dan list2
        # agar node dengan nilai lebih kecil selalu menjadi yang pertama
        if list1.val > list2.val:
            list1, list2 = list2, list1
        
        # Gabungkan sisa dari list1.next dengan list2 secara rekursif
        list1.next = self.mergeTwoLists(list1.next, list2)
        
        # Kembalikan node awal (list1) sebagai head dari linked list gabungan
        return list1
