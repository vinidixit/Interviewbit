# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 18:35:47 2018

@author: I309535
"""
"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Given intervals [1,3],[6,9] insert and merge [2,5] would result in [1,5],[6,9].

Example 2:

Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] would result in [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

Make sure the returned intervals are also sorted.
"""
##********** ASKED in GOOGLE ##

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def in_range(self, start,end, num):
        return num>=start and num<=end
    
    def is_overlap(self,ind_str):
        return len(ind_str.split('_'))==1
        
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
        n = len(intervals)
        if n == 0:
            return [new_interval]
        res=[]
        s_ind =None
        e_ind =None
        for i in range(n):
            if s_ind!=None and e_ind!=None:
                break
            interval = intervals[i]
            if self.in_range(interval.start,interval.end, new_interval.start):
                s_ind = str(i)
            if self.in_range(interval.start,interval.end, new_interval.end):
                e_ind = str(i)
            
            if i < n-1:
                next_interval = intervals[i+1]
                ## non overlap
                if self.in_range(interval.end,next_interval.start, new_interval.start):
                    s_ind = str(i+1)+'_'
                if self.in_range(interval.end,next_interval.start, new_interval.end):
                    e_ind = str(i+1)+'_'
            
            if i ==0:
                if new_interval.start<interval.start:
                    s_ind = str(0)+'_'
                if new_interval.end<interval.start:
                    e_ind = str(0)+'_'
            if i == n-1:
                if new_interval.start>interval.end:
                    s_ind = str(n)+'_'
                if new_interval.end>interval.end:
                    e_ind = str(n)+'_'
                    
            
        new_s = int(s_ind.split('_')[0])
        new_e = int(e_ind.split('_')[0])
        res = intervals[0:new_s]
        
        if self.is_overlap(s_ind):
            cur_interval = intervals[new_s]
            new_interval.start = min(new_interval.start,cur_interval.start)
        if self.is_overlap(e_ind):
            cur_interval = intervals[new_e]
            new_interval.end = max(new_interval.end,cur_interval.end)
        
        res.append(new_interval)
        if self.is_overlap(e_ind):
            res = res+intervals[(new_e+1):]
        else:
            res = res+intervals[new_e:]
        
        return res
        