# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 21:20:40 2018

@author: I309535
"""

# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
from collections import deque

# @param A : root node of tree
# @return a list of list of integers
def levelOrder(A):
    q = deque()
    if A==None:
        return []
    
    q.append(A)
    q.append('#')
    result = []
    cur_level = []
    while len(q)>1:
        cur = q.popleft() 
        if cur == '#':
            result.append(list(cur_level))
            cur_level = []
            q.append('#')
        else:
            cur_level.append(cur.val)
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
                
    if len(cur_level)>0:
        result.append(cur_level)
    return result
                
                    
root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
node1.left = TreeNode(4)
node1.right = TreeNode(5)
node2.left = TreeNode(6)
node2.right = TreeNode(7)

root.left = node1
root.right = node2

print levelOrder(root)