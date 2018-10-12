# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 15:02:15 2018

@author: I309535
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBSTAux(self,A,lower,upper):
        if A == None:
            return True
        
        isValidRoot = not (A.val < lower or A.val>=upper)
        leftStatus = self.isValidBSTAux(A.left,lower,A.val)
        rightStatus = self.isValidBSTAux(A.right,A.val,upper)
        
        return isValidRoot and leftStatus and rightStatus
        
    # @param A : root node of tree
    # @return an integer
    def isValidBST(self, A):
        status = self.isValidBSTAux(A,0,2147483647)
        return 1 if status else 0
