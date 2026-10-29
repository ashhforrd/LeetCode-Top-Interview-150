# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        output = ListNode()
        temp = output

        if not lists or len(lists) == 0: return

        listMap = {}
        for i in range(len(lists)):
            l = lists[i]
            while l:
                if l.val not in listMap:
                    listMap[l.val] = 1
                else:
                    listMap[l.val] += 1
                l = l.next
        
        sortedMap = dict(sorted(listMap.items()))

        for key in sortedMap:
            for i in range(sortedMap[key]):
                temp.next = ListNode(key)
                temp = temp.next
        
        return output.next
