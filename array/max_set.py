# -*- coding: utf-8 -*-
"""
Created on Mon Apr 02 11:38:55 2018

@author: I309535
"""

class MaxNonNegativeSubarray:
    
    def test_subarray(self,cur_sum,max_sum,cur_lr,max_lr):
        if max_lr[0] == None:
            return True
        
        if cur_sum > max_sum:
            return True
        
        cur_windowlen = cur_lr[1]-cur_lr[0]
        max_window_len = max_lr[1]-max_lr[0]
        
        if cur_sum == max_sum and cur_windowlen>max_window_len:
            return True
        
        if cur_sum == max_sum and cur_windowlen==max_window_len and cur_lr[0]<max_lr[0]:
            return True
        
        return False
        
    def maxset(self, A):
        lp,n = None,len(A)
        max_l,max_r,max_sum = None,None,None
        
        for i in range(n):
            if A[i] >=0:
                #print 'pos:',A[i]
                if lp==None:
                    lp = i
            else:
                #print 'neg:', A[i], lp
                if lp != None:
                    cur_sum = sum(A[lp:i])
                    print cur_sum,max_sum
                    do_update = self.test_subarray(cur_sum,max_sum,(lp,i),(max_l,max_r))
                    
                    if do_update:
                        max_sum = cur_sum
                        max_l,max_r = lp,i
                    # reset left pointer
                    lp = None
        
        if lp != None:
            cur_sum = sum(A[lp:])
            do_update = self.test_subarray(cur_sum,max_sum,(lp,i),(max_l,max_r))
            if do_update:
                max_sum = cur_sum
                max_l,max_r = lp,n
            
        
        print max_l,max_r
        if max_l !=None:
            return A[max_l:max_r]
    
        return []        
        
        
        
s = MaxNonNegativeSubarray()
A = [ 756898537, -1973594324, -2038664370, -184803526, 1424268980 ]
print s.maxset(A)




