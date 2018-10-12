# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 21:43:37 2018

@author: I309535
"""

class Solution:
    def isValidPosition(self, board, q, pos):
        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c]=='Q' and (c==pos or abs(r-q)==abs(c-pos)):
                    return False
        return True
                
    def solveNQueensHelper(self, board, n, q, result):
        if q == n:
            boardStr = [''.join(row) for row in board]
            result.append(boardStr)
            
            return
        print board,'\n'
        for c in range(n):
            if self.isValidPosition(board, q, c):
                board[q][c] = 'Q'
                self.solveNQueensHelper(board, n, q+1, result)
                board[q][c] = '.'
            
    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(self, A):
        board = [list('.'*A) for _ in range(A)]
        result = []
        self.solveNQueensHelper(board, A, 0, result)
        return result
        
print Solution().solveNQueens(6)