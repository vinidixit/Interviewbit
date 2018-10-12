# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 20:29:49 2018

@author: I309535
"""

def gen_combinations(A,cur_ind,comb,target,result):
    if sum(comb) == target:
        #print 'result:',comb
        result.append(comb)
        return
    
    if sum(comb)>target:
        print 'Sum more than target,returning..'
        return
    
    # keeping cur_ind as starting point of comb
    for i in range(cur_ind,len(A)):
        comb.append(A[i])      
        print 'before:',comb
        gen_combinations(A,i,list(comb),target,result)
        comb = comb[:-1] #remove current element to consider next
        
        print cur_ind,'After:',comb,'\n'
        
        
# @param A : list of integers
# @param B : integer
# @return a list of list of integers
def combinationSum( A, B):
    result = []
    gen_combinations(A,0,[],B,result)
    return result

A = [ 8, 10, 6, 11, 1, 16, 8 ]
target = 12
A = set(A) ######## ** IMP STEPS
sorted(A) #########
print combinationSum(list(A),target)