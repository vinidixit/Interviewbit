# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 18:36:31 2018

@author: I309535
"""

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    
    def sortedMerge(self, list1, list2):
        if not list1 and not list2:
            return
        if not list1:
            return list2
        if not list2:
            return list1
        
        result = None
        if list1.val<list2.val:
            result = list1
            list1 = list1.next
        else:
            result = list2
            list2 = list2.next
        
        cur = result
        while list1 and list2:
            if list1.val<list2.val:
                cur.next = list1
                list1 = list1.next
                cur = cur.next
            else:
                cur.next = list2
                list2 = list2.next
                cur = cur.next
        
        if list1:
            cur.next = list1
        if list2:
            cur.next = list2
        return result
    
    def getMiddle(self, A):
        slow,fast = A,A.next
        while fast:
            fast = fast.next
            if not fast:
                break
            slow = slow.next
            fast = fast.next
            
        return slow
        
    def mergeSort(self, A):
        if not A:
            return
        
        midNode = self.getMiddle(A)
        print midNode, midNode.val
        rightList = midNode.next
        midNode.next = None
        
        if not rightList:
            return A
        
        left = self.mergeSort(A)
        right = self.mergeSort(rightList)
        sortedList = self.sortedMerge(left, right)
        return sortedList
        
    # @param A : head node of linked list
    # @return the head node in the linked list
    def sortList(self, A):
        return self.mergeSort(A)
        
        
l = ListNode(1)
Solution().sortList(l)

        