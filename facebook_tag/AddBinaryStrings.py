# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 15:05:25 2018

@author: I309535
"""

# @param A : string
# @param B : string
# @return a strings
def addBinary(self, A, B):
    r1,r2 = len(A)-1,len(B)-1
    carry = 0
    res = ''
    while r1>=0 and r2>=0:
        b1,b2 = int(A[r1]),int(B[r2])
        r1-=1
        r2-=1
        b_sum = b1^b2^carry
        carry = (b1 and b2) or(b1 and carry) or (b2 and carry)
        res = str(b_sum)+res
    
    while r1 >=0:
        b1 = int(A[r1])
        b_sum = b1^carry
        carry = b1 and carry
        res = str(b_sum)+res
        r1-=1
    
    while r2 >=0:
        b2 = int(B[r2])
        b_sum = b2^carry
        carry = b2 and carry
        res = str(b_sum)+res
        r2-=1
        
    if carry!=0:
        res = str(carry)+res
        
    return res