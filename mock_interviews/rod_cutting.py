# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 09:05:06 2018

@author: I309535
"""

class Solution:
    """
 1 2 3 4 5 6
 * *     *
"""
    def find_cost(self,l, r, markers):
        # l <= marker <= r
        cost = r-l+1
        return cost
        
    def find_total_cost(self,markers,rod_len,total_cost):
        l,r = 0,len(markers)-1
        
        if l >= r:
            return
        
        mid = l + (r-l)/2
        
        total_cost[0] += r-l+1
        total_cost[0] += self.find_cost(l,mid-1,markers)
        total_cost[0] += self.find_cost(mid+1,r,markers)
        
        
    # @param A : integer
    # @param B : list of integers
    # @return a list of integers
    def rodCut(self, A, B):
        N = A # size of rod
        markers = B # list of markers
        
        total_cost = list([0])
        self.find_total_cost(markers,N,total_cost)
        
        return total_cost[0]
        
        
        
