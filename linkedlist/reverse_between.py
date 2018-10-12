# -*- coding: utf-8 -*-
"""
Created on Mon Apr 09 15:46:56 2018

@author: I309535
"""

# @param A : head node of linked list
# @param B : integer
# @param C : integer
# @return the head node in the linked list
def reverseBetween(A, B, C):
    head,m,n = A,B,C
    sublist1_head = ListNode('dummy')
    sublist1_tail = sublist1_head
    sublist1_head.next = head
    
    curInd = 1
    while sublist1_tail.next and curInd < m:
        sublist1_tail = sublist1_tail.next
        curInd+=1
    
    if sublist1_tail == None:
        return sublist1_head.next
    
    print 'list1 tail:',sublist1_tail.val
    
    prev= None # for now, contains head of sublist3
    cur = head.next
    sublist2_tail = sublist1_tail.next
    while cur and curInd < n: #check boundary
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node
        curInd+=1
    
    sublist2_head = prev
    sublist3_head = cur
    sublist1_tail.next = sublist2_head
    print 'list2 head:',sublist2_head.val
    print 'list2 tail:',sublist2_tail.val
    if sublist2_tail != None:
        sublist2_tail.next = sublist3_head
    
    print_list(sublist1_head)
    print_list(sublist1_tail)
    return sublist1_head.next


class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
    
def print_list(head):
    tmp = head
    while tmp:
        print tmp.val,
        tmp = tmp.next
    print '\n'
        
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

print_list(head)
print_list(reverseBetween(head,1,2))
print_list(head)


    
    
    
    
    