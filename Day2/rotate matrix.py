class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols  =  len(matrix[0])
        #This logic is correct but will not work here as we have to make in place changes.
        # for i in range(0,cols):
        #     for j in range(rows-1,-1,-1):
        #        print(matrix[j][i] )
                
        #Transpose the matrix
        for i in range(rows):
            for j in range(i,cols):
                matrix[i][j],matrix[j][i] = matrix[j][i] ,matrix[i][j] 
        
        for i in range(rows):
            for j in range(rows//2):
                matrix[i][j],matrix[i][rows-j-1] = matrix[i][rows-j-1] ,matrix[i][j]


