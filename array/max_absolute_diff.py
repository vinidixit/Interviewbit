"""
Maximum Absolute Difference
You are given an array of N integers, A1, A2 ,…, AN. Return maximum value of f(i, j) for all 1 ≤ i, j ≤ N.
f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.

For example,

A=[1, 3, -1]

f(1, 1) = f(2, 2) = f(3, 3) = 0
f(1, 2) = f(2, 1) = |1 - 3| + |1 - 2| = 3
f(1, 3) = f(3, 1) = |1 - (-1)| + |1 - 3| = 4
f(2, 3) = f(3, 2) = |3 - (-1)| + |2 - 3| = 5

So, we return 5.
"""
class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        n = len(A)
		# |A[i] - A[j]| + |i - j| => +-(A[i]-A[j]) +- (i-j)
		# => (A[i]+- i) - (A[j] +- j)
        A_sum = [A[i]+i for i in range(n)]
        A_minus = [A[i]-i for i in range(n)]
        
        A_sum.sort()
        A_minus.sort()
        
        return max(A_sum[-1]-A_sum[0],A_minus[-1]-A_minus[0])