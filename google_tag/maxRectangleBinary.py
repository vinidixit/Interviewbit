class Solution:
    # @param A : list of list of integers
    # @return an integer
    def maximalRectangle(self, A):
        if not A:
            return 0
        
        ROW,COL = len(A),len(A[0])
        max_area = 0
        connected_grid = [[(0,0)]*(COL+1) for _ in (ROW+1)]
        
        for i in range(1,ROW+1):
            for j in range(1,COL+1):
                if A[i-1][j-1]==1:
                    row_len1 = connected_grid[i][j-1][0]+1
                    col_len1 = connected_grid[i][j-1][1]
                    row_len2 = connected_grid[i-1][j][0]
                    col_len2 = connected_grid[i-1][j][1]+1
                    
A = [[0]*3 for _ in range(3)]            
A[0] = [1,1,1]
A[1] = [0,1,1]
A[2] = [1,0,0] 
    

print Solution().maximalRectangle(A)