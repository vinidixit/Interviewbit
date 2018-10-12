# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
import heapq
class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        result = ListNode('head')
        resPtr = result
        heap = []
        
        for i in range(len(A)):
            heapq.heappush(heap,(A[i].val,i))
        
        while len(heap) > 0:
            curMinVal,listPtr = heapq.heappop(heap)
            resPtr.next = A[listPtr]    
            resPtr = resPtr.next
            if A[listPtr].next!=None:
                A[listPtr] = A[listPtr].next
                heapq.heappush(heap,(A[listPtr].val,listPtr))
        
        return result.next
        
