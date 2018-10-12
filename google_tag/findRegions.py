class Solution:
    def markUncaptured(self, A, i, j, ROW, COL):
        if not (0<=i<ROW and 0<=j<COL) or A[i][j] in ['+','X']:
            return
        
        A[i][j] = '+'
        self.markUncaptured(A, i-1, j, ROW, COL)    
        self.markUncaptured(A, i+1, j, ROW, COL)    
        self.markUncaptured(A, i, j-1, ROW, COL)    
        self.markUncaptured(A, i, j+1, ROW, COL)    
    
    def findRegions_2(self, A,ROW,COL):
        for j in range(COL):
            self.markUncaptured(A, 0, j, ROW, COL)    
            self.markUncaptured(A, ROW-1, j, ROW, COL)    
            
        for i in range(ROW):
            self.markUncaptured(A, i, 0, ROW, COL)    
            self.markUncaptured(A, i, COL-1, ROW, COL)    
        
        for i in range(ROW):
            for j in range(COL):
                if A[i][j] == 'O':
                    A[i][j] = 'X'
                if A[i][j] == '+':
                    A[i][j] = 'O'
                    
    # @param A : list of list of chars
    def solve(self, A):
        if not A:
            return
        ROW,COL = len(A),len(A[0])
        self.findRegions_2(A,ROW,COL)
                    
                    