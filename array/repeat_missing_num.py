"""
Repeat and Missing Number Array
You are given a read only array of n integers from 1 to n.

Each integer appears exactly once except A which appears twice and B which is missing.

Return A and B.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Note that in your output A should precede B.
"""
class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        n = len(A)
        A_sum = sum(A)
        n_sum = n*(n+1)/2
        sum_diff = n_sum-A_sum
        
        A_sq_sum = sum([a*a for a in A])
        n_sq_sum = n*(n+1)*(2*n+1)/6
        sq_sum_diff = n_sq_sum-A_sq_sum
        
        b = int(0.5*(sq_sum_diff/sum_diff + sum_diff))
        a = int(b-sum_diff)
        return [a,b]