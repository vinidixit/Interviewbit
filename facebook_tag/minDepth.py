# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 17:54:41 2018

@author: I309535
"""

# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


# @param A : root node of tree
# @return an integer
def minDepth(A):
    if A == None:
            return 0
            
    if A.left==None and A.right==None:
        return 1
    
    if A.left==None:
        return 1+minDepth(A.right)
    
    if A.right==None:
        return 1+minDepth(A.left)    
    
    lh = minDepth(A.left)
    rh = minDepth(A.right)
    return 1+min(lh,rh)

    
root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
root.left = node1
root.right = node2
node1.left = TreeNode(4)
node1.right = TreeNode(5)
node2.left = TreeNode(6)
node2.right = TreeNode(7)

print minDepth(root)