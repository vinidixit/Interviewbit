"""
Min Steps in Infinite Grid
You are in an infinite 2D grid where you can move in any of the 8 directions :

 (x,y) to 
    (x+1, y), 
    (x - 1, y), 
    (x, y+1), 
    (x, y-1), 
    (x-1, y-1), 
    (x+1,y+1), 
    (x-1,y+1), 
    (x+1,y-1) 
You are given a sequence of points and the order in which you need to cover the points. Give the minimum number of steps in which you can achieve it. You start from the first point.

Example :

Input : [(0, 0), (1, 1), (1, 2)]
Output : 2
It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).
"""


class Solution:
    
    def get_min_steps(self,point1,point2):
        r_diff = abs(point2[0]-point1[0])
        c_diff = abs(point2[1]-point1[1])
        
        ## diagonal movement
        diag_steps = min(r_diff,c_diff)
        r_diff -= diag_steps
        c_diff -= diag_steps
    
        ## diagonal, row or column movement
        min_steps = diag_steps+r_diff+c_diff
        return min_steps   
        
        
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        n = len(A)
        total_min_steps = 0
        for i in range(n-1):
           total_min_steps+= self.get_min_steps((A[i],B[i]),(A[i+1],B[i+1]))
        
        return total_min_steps
        