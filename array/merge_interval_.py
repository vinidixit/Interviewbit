# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 09:50:06 2018

@author: Vini Dixit
"""

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

"""
Merge overlapping intervals and return in sorted order
"""
class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        intervals.sort(key = lambda x:x.start)
        n = len(intervals)
        i = 0
        res = []
        while i < n:
            cur_interval = intervals[i]
            if i == n-1:
                res.append(cur_interval)
                break
            
            cur_e = cur_interval.end
            # go to next interval
            j = i+1
            
            while j < n and cur_e >= intervals[j].start:
                overlap_interval = intervals[j]
                cur_e = max(overlap_interval.end,cur_e)
                j+=1
                
            cur_interval.end = cur_e
            res.append(cur_interval)
            i = j
            
        return res
