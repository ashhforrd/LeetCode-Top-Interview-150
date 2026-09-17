# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0

        if not head:
            return None
        if k == 0:
            return head

        # Dapatkan length dari head, kemudian k mod by length
        track = head
        while track:
            length += 1
            track = track.next

        # Algoritma nya bikin node baru kemudian node nextnya itu head, dan mematikan node yang ada di ujung
        # atau mendapatkan sebanyak n (rotate) elemen terakhir buat node baru, dan hasil nodenya dihubungin dengan head, dan mematikan node terkahir sebanyak rotate
        
        rotate = k % length
        firstTotal = length - rotate

        early = ListNode()
        earlyPointer = early
        for i in range(firstTotal):
            earlyPointer.next = ListNode(head.val)
            earlyPointer = earlyPointer.next
            head = head.next
                            
        output = ListNode()
        outputPointer = output
        while head:
            outputPointer.next = ListNode(head.val)
            outputPointer = outputPointer.next
            head = head.next
                
        outputPointer.next = early.next
        
        return output.next