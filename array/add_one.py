# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 09:42:34 2018

@author: I309535
"""

class Solution:
	# @param A : list of integers
	# @return a list of integers
	def plusOne(self, A):
         n=len(A)
         
         c=1
         res = [0]*n
         
         for i in range(n,0,-1):
             s = A[i-1]+c
             c = int(s/10)
             res[i-1]=s%10
             
         if c!=0:
             res.insert(0,c)   
         i=0
         while i<len(res) and res[i]==0:
             i+=1
         res = res[i:]   
         return res