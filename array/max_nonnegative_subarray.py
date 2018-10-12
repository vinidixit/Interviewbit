"""
Find out the maximum sub-array of non negative numbers from an array.
The sub-array should be continuous. That is, a sub-array created by choosing the second and fourth element and skipping the third element is invalid.

Maximum sub-array is defined in terms of the sum of the elements in the sub-array. Sub-array A is greater than sub-array B if sum(A) > sum(B).

Example:

A : [1, 2, 5, -7, 2, 3]
The two sub-arrays are [1, 2, 5] [2, 3].
The answer is [1, 2, 5] as its sum is larger than [2, 3]
NOTE: If there is a tie, then compare with segment's length and return segment which has maximum length
NOTE 2: If there is still a tie, then return the segment with minimum starting index
"""

class Solution:
    
    def update_best_set(self,i,j,best_i,best_j,A):
        if best_i==-1:
            return i,j
            
        cur_sum = sum(A[i:(j+1)])
        best_sum = sum(A[best_i:(best_j+1)])
        if cur_sum>best_sum or (cur_sum==best_sum and (j-i>best_j-best_i)):
            return i,j
        return best_i,best_j
            
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        i = -1
        j = -1
        best_i=-1
        best_j =-1
        for it in range(len(A)):
            if A[it] < 0:
                if i !=-1:
                    j = it-1
                    # update
                    best_i,best_j = self.update_best_set(i,j,best_i,best_j,A)
                    i=-1
                    j=-1
            else:        
                if i == -1:
                    i=it
                    
        if i!=-1 and j==-1:
            j = len(A)-1
            best_i,best_j = self.update_best_set(i,j,best_i,best_j,A)
                    
        return A[best_i:(best_j+1)]            
                    
                    
