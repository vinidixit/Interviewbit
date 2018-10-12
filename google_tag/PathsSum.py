# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 11:29:00 2018

@author: I309535
"""

# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def findPathsSum(self, A, sumObj, pathNum):
        if not A:
            return
        if A.left==None and A.right==None:
            sumObj[0] += (pathNum*10+A.val)
            return
        
        self.findPathsSum(A.left, sumObj, pathNum*10+A.val)
        self.findPathsSum(A.right, sumObj, pathNum*10+A.val)
        
    # @param A : root node of tree
    # @return an integer
    def sumNumbers(self, A):
        sumObj = [0]
        self.findPathsSum(A, sumObj, 0)
        return sumObj[0]
        

root = TreeNode(5)
root.left = TreeNode(2)
root.left.left = TreeNode(1)

print Solution().sumNumbers(root)