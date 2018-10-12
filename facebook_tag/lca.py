# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 14:15:28 2018

@author: I309535
"""

# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


def search_node(root,search_key):
    stack = list()
    search_status = search_node_helper(root,search_key,stack)
    return stack
    
def search_node_helper(root,key,stack):
    if root == None:
        return False
    
    stack.append(root)
    
    if root.val==key:
        return True
    
    print 'before left:',[node.val for node in stack]
    left_status = search_node_helper(root.left,key,stack)
    print 'after left:',[node.val for node in stack]
    right_status = search_node_helper(root.right,key,stack)
    print 'after right:',[node.val for node in stack],'\n'
    
    if left_status or right_status:
        return True
    
    stack.pop()
    return False

root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
root.left = node1
root.right = node2
node1.left = TreeNode(4)
node1.right = TreeNode(5)
node2.left = TreeNode(6)
node2.right = TreeNode(7)

print search_node(root,7)



"""
# @param A : root node of tree
# @param B : integer
# @param C : integer
# @return an integer
def lca(A, B, C):
    root = A
    path1 = search_node(root,B)
    path2 = search_node(root,C)
    
    lca = None
    i = 0
    while i < len(path1) and i<len(path2) and path1[i]==path2[i]:
        lca = path1[i]
        i += 1
    
    if lca:
        return lca.val
    return -1
""" 
    
