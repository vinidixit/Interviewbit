# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 15:14:42 2018

@author: I309535
"""

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, A, B):
        if not A and not B:
            return
        m = len(A)
        n = len(B)
        if m==0:
            print n
            return self.findMedian(B,0,n-1)[1]
        
        if n==0:
            return self.findMedian(A,0,m-1)[1]
        print m,n   
        return self.findMedianAB(A,0,m-1,B,0,n-1)
    
    def findMedian(self,A,l,r):
        mid = l + (r-l)/2
        if r-l %2 == 0:
            return mid,A[mid]
        print 'rl:',r,l
        median = (A[mid]+A[mid+1])/2.0
        return mid,median
    
    def findMedianShort(self,A,l1,r1,B,l2,r2):
        m,n = r1-l1,r2-l2
        mid = (m+n)/2
        median = [None,None]
        i,j = 0,0
        while i < m and j < n:
            temp = None
            if A[i] < A[j]:
                temp,i = A[i],i+1
            elif A[i] > A[j]:
                temp,j = A[j],j+1
            else:
                temp,i,j = A[i],i+1,j+1
                
            if i+j == mid+1:
                if median[0]==None:
                    median = [temp,temp]
                else:
                    median[1] = temp
                break
            if i+j == mid:
                median[0] = temp
                
        if (m+n)%2==0:
            return median[0]
        return (median[0]+median[1])/2.0
        
    def findMedianAB(self,A,l1,r1,B,l2,r2):
        if r1-l1==0 and r2-l2==0:
            return
        if r1-l1==0:
            return self.findMedian(B,l2,r2)[1]
        if r2-l2==0:
            return self.findMedian(A,l1,r1)[1]
        #if r1-l1<=1 or 0<=r2-l2<=1:
        #    return self.findMedianShort(A,l1,r1,B,l2,r2)
        
           
        mid1,median1 = self.findMedian(A,l1,r1)
        mid2,median2 = self.findMedian(B,l2,r2)
        
        if median1== median2:
            return median1
        if median1 < median2:
            return self.getMedianAB(A,mid1,r1,B,l2,mid2)
        return self.getMedianAB(A,l1,mid1,B,mid2,r2)
        
        
print Solution().findMedianSortedArrays([],[20])        
        
        
        
        