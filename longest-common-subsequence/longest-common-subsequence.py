class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        matrix  = [[0]*(n2+1) for _ in range(n1+1)]
        for col in reversed(range(len(text2))):
            for row in reversed(range(len(text1))):
                if text2[col] == text1[row]:
                    matrix[row][col] = 1+matrix[row+1][col+1]
                else:
                    matrix[row][col] = max(matrix[row][col+1],matrix[row+1][col])
        return matrix[0][0]
    
                    
            
        
        