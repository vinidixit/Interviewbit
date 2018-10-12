# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 18:05:12 2018

@author: I309535
"""

def buildHeap(self, A):
        n = len(A)
        for i in range(n/2,-1,-1):
            self.heapify(A,i,n)
    
    def heapify(self, A, i, n):
        left,right = 2*i+1,2*i+2
        largest = i
        if left<n and A[largest]<A[left]:
            largest = left
        if right<n and A[largest]<A[right]:
            largest = right
        if largest != i:
            A[largest],A[i] = A[i],A[largest] 
            self.heapify(A,largest)
    
    def heapsort(self, A):
        self.buildHeap(A)
        n = len(A)
        for i in range(n):
            A[i],A[n-i-1] = A[n-i-1],A[i]
            self.heapify(A,i,n-1)
            
    # @param A : head node of linked list
    # @return the head node in the linked list
    def sortList(self, A):
        self.heapsort(A)