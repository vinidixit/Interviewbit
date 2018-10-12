# -*- coding: utf-8 -*-
"""
Created on Thu May 31 21:38:39 2018

@author: I309535
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
   -3
  2    3 
-2 8
5
"""
class Solution:
    # @param A : root node of tree
    # @return an integer
    def maxPathSum(self, A):
        if not A:
            return 
        maxSum = list([float('-inf')])
        self.maxPathSumAux(A, maxSum)
        return maxSum[0]
    
    def maxPathSumAux(self, tree, maxSum):
        if tree == None:
            return 0
        
        ls = self.maxPathSumAux(tree.left, maxSum)
        rs = self.maxPathSumAux(tree.right, maxSum)
        
        maxSum[0] = max(maxSum[0],ls+ rs + tree.val)
        maxSum[0] = max(maxSum[0],tree.val)
        
        return max(ls,rs)+tree.val
        
        
            