# -*- coding: utf-8 -*-
"""
Created on Thu May 24 13:26:23 2018

@author: I309535
"""

def maxRectArea(binGrid):
    row = len(binGrid)
    col = len(binGrid[0])
    
    connectedVals = [0]*row
    connectedVals = [[0]*col for i in range(row)]
    
    connectedVals[0][0] = 1 if binGrid[0][0]==1 else 0
    maxArea = 0
    
    for c in range(1,col):
        if binGrid[0][c] == 1:
            connectedVals[0][c] = connectedVals[0][c-1]+1
            maxArea = max(maxArea, connectedVals[0][c])
    
    for r in range(1,row):
        for c in range(col):
            if binGrid[r][c] == 1 and binGrid[r-1][c]==1:
                connectedVals[0][c] = connectedVals[0][c-1]+1
                maxArea = max(maxArea, connectedVals[0][c])