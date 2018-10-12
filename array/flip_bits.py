# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 20:34:06 2018

@author: I309535
"""

class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        l_opt = None
        r_opt = None
        max_len = 0
        
        for i in range(len(A)):
            if A[i]=='0':
                l_opt = i
                r_opt = i
                break
        
        if l_opt == None:
            return []
        
        zero_cnt = 0
        one_cnt = 0
        max_len = 1
        
        l = l_opt
        for i in range(l_opt,len(A)):
            if A[i]=='0':
                if l == None:
                    l = i
                zero_cnt += 1
            else:
                if l!=None:
                    one_cnt += 1
            
            one_len = zero_cnt-one_cnt
            if one_len > max_len:
                l_opt = l
                r_opt = i
                max_len = one_len
                
            if one_len == 0:
                # rest
                l,zero_cnt,one_cnt = None,0,0
                
        one_cnt = len(A[A==1])
        print(max_len)
        return [l_opt+1,r_opt+1]
        
        #return []


s = Solution()
print(s.flip('1101010001'))


