# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 19:45:49 2018

@author: I309535
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 15:53:48 2018

@author: I309535
"""

def findKPartition(A,k):
    arr_sum = sum(A)
    if arr_sum%k != 0:
        return False
    
    sub_sum = arr_sum/k
    n = len(A)
    return findKPartitionAux(A,sub_sum,sub_sum,0,k,n,set())

def findKPartitionAux(A,cur_sum,sub_sum,temp_k,k,n,taken, maxSubsetSum, result):
    if temp_k==k:
        subsetSum
        return True
    
    if n == 0:
        return False
    
    if cur_sum==0:
        cur_sum = sub_sum
        temp_k += 1
        
    if A[n-1]>cur_sum or (n-1) in taken:
        return findKPartitionAux(A,cur_sum,sub_sum,temp_k,k,n-1,taken)
    taken.add(n-1)
    inc = findKPartitionAux(A,cur_sum-A[n-1],sub_sum,temp_k,k,n,taken)
    taken.remove(n-1)
    
    ex = findKPartitionAux(A,cur_sum,sub_sum,temp_k,k,n-1,taken)   
    return ex or inc

A = [4, 3, 2, 3, 5, 2, 1] 
k = 4
print findKPartition(A,k)