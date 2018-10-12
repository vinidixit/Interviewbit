# -*- coding: utf-8 -*-
"""
Created on Mon Apr 02 12:24:20 2018

@author: I309535
"""

class GeneratePascalTriangle:
    # @param A : integer
    # @return a list of list of integers
    def generate(self, A):
        res = []
        n = A
        if n == 0:
            return res
            
        res.append([1])
        
        for i in range(1,n):
            last_row = res[i-1]
            cur_row = [1]
            for j in range(1,len(last_row)):
                cur_row.append(last_row[j-1]+last_row[j])
            
            cur_row.append(1)
            res.append(cur_row)
            
        return res
    
    # Using O(k) space
    def generate_kth_row(self, k):
        n = k
        last_row = [1]
        
        for i in range(1,n+1):
            cur_row = [1]
            for j in range(1,len(last_row)):
                cur_row.append(last_row[j-1]+last_row[j])
            
            cur_row.append(1)
            last_row = cur_row
            
        return last_row
        
        
        
        
gps = GeneratePascalTriangle()
#print gps.generate(5)

print gps.generate_kth_row(5)




