"""
Max Sum Contiguous Subarray
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example:

Given the array [-2,1,-3,4,-1,2,1,-5,4],

the contiguous subarray [4,-1,2,1] has the largest sum = 6.

For this problem, return the maximum sum.
"""
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        n = len(A)
        max_sum = None
        cur_sum = 0
        for i in range(n):
            cur_sum += A[i]
            max_sum = cur_sum if max_sum==None else max(max_sum,cur_sum)
            
            if cur_sum <0:
                cur_sum = 0    
                
        return max_sum