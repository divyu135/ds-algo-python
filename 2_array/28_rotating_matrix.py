def rotating_by_90_degree( matrix ):
    n = len(matrix)
    for i in range(n):
        for j in range(n//2):
            matrix[i][j],matrix[i][-j-1] = matrix[i][-j-1],matrix[i][j]
    for i in range(n):
        for j in range(i,n):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

    print(*matrix,sep="\n")

if __name__ == '__main__':
    mat = [ [1, 2, 3, 4 ], 
        [5, 6, 7, 8 ], 
        [9, 10, 11, 12 ], 
        [13, 14, 15, 16 ] ] 
    rotating_by_90_degree(mat)
    print()
    mat = [ [1, 2, 3 ], 
        [4, 5, 6 ], 
        [7, 8, 9 ] ] 
    rotating_by_90_degree(mat)
    print()
    mat = [ [1, 2 ], 
        [4, 5 ] ] 
    rotating_by_90_degree(mat)