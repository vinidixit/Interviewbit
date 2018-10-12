# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 11:02:11 2018

@author: I309535
"""

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return an integer
    def canCompleteCircuit(self, A, B):
        station_cover = 0
        fuel = 0
        start = 0
        n = len(A)
        visit = [False]*len(A)
        while station_cover < len(A) and not visit[start]:
            visit[start] = True
            for i in range(start,len(A)):
                station_cover += 1
                fuel += A[i]-B[i]
                if station_cover == n+1:
                    break
                if fuel < 0:
                    start,fuel,station_cover = (i+1)%n,0,0
                    break
                    
            if station_cover == 0:
                continue
            
            for i in range(0,start+1):
                station_cover += 1
                fuel += A[i]-B[i]
                if station_cover == n+1:
                    break
                if fuel < 0:
                    start,fuel,station_cover = (i+1)%n,0,0
                    break
        return start if station_cover==n+1 else -1         
                
A = [ 684, 57, 602, 987 ]
B = [ 909, 535, 190, 976 ]
print Solution().canCompleteCircuit(A,B)