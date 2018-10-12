# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 22:12:20 2018

@author: I309535
"""

from collections import deque
class Solution:
    # @param start : string
    # @param end : string
    # @param dictV : list of strings
    # @return a list of list of strings
    def findLadders(self, start, end, dictV):
        q = deque()
        q.append([start])
        result = []
        minDist = float('inf')
        
        while q:
            curList = q.popleft()
            curString = curList[-1]
            if curString==end:
                if minDist>=len(curList):
                    result.append(curList)
                    minDist = len(curList)
                else:
                    break
                
            for i in range(len(curString)):
                for j in range(ord('a'),ord('z')+1):
                    newString = ''.join([curString[:i],chr(j),curString[i+1:]])
                    if newString in dictV or newString==end:
                        newList = list(curList)
                        newList.append(newString)
                        q.append(newList)
                        
        return result
                
                
d = ["hot","dot","dog","lot","log"]
print Solution().findLadders('hit','cog',d)

                