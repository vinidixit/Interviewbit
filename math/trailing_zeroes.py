# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 21:15:43 2018

@author: I309535
"""

class Solution:
    
    """
    n = 5
    1 2 3 4 5
    10_count = 0
    2_count = 1+2
    5_count = 1
    
    c(2,5) = 1
    
    n = 23
    c(5) = 1-10 -> 1, 11-20-> 1, 21-23->0
    c(10) = 2
    2 + 2 = 4
    
    n = 28
    c(5^p) = 1 -> 5,25,125,..
    c(5) = 1+1+1
    c(10) = 2
    
    n = 78
    c(10) = 6 - 10,20,30,40,50(5*10),60,70
    c(5^p) = 1 - 25
    c(5) = 9 - 5,15,25,35,45,55,65,75,  50
    17
    
   78! => 18
   5^1 = 15
   5^2 = 25, 50, 75
   
   100 -> 10
   4617! = 
   5^1 -> 48
   5^2 -> 
  
    """
    
    def get_factor_counts(self,num,base,inc):
        i = 1
        count = 0
        product = base * i
        while product<=num:
            count += 1
            i += inc
            product = base * i
            
        return count    
                  
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        base = 5
        count = 0
        count += self.get_factor_counts(A,base,2)
        count += int(A/10)
        
        i = 2
        while pow(5,i) <= A:
            base = pow(5,i)
            print 1
            count += self.get_factor_counts(A,base,1)
            i+=1
            
        return count
        
