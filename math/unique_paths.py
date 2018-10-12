# -*- coding: utf-8 -*-
"""
Created on Mon Apr 02 10:23:01 2018

@author: I309535
"""

class UniquePaths:
    def uniquePaths(self, A, B):
        grid = [0]*A
        
        for i in range(A):
            grid[i] = [0]*B
        
        ## right moves
        for i in range(0,B):
            grid[0][i] = 1
        
        ## down moves
        for i in range(1,A):
            grid[i][0] = 1
        
        for r in range(1,A):
            for c in range(1,B):
                grid[r][c] = grid[r-1][c]+grid[r][c-1]
                
        return grid[-1][-1]