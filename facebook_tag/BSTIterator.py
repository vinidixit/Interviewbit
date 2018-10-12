# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 18:14:40 2018

@author: I309535
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.root = root
        self.stack = list()
        tmp = root
        while tmp:
            self.stack.append(tmp)
            tmp = tmp.left
        
    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return len(self.stack)>0

    # @return an integer, the next smallest number
    def next(self):
        minNode = self.stack.pop()
        if minNode.right:
            cur_node = minNode.right
            while cur_node:
                self.stack.append(cur_node)
                cur_node = cur_node.left
        
        return minNode.val

# Your BSTIterator will be called like this:
# i = BSTIterator(root)
# while i.hasNext(): print i.next(),
