def zigzag(matrix):
    row = len(matrix)
    if row == 0:
        return
    col = len(matrix[0])
    for i in range(row):
        if i % 2 == 0:
            for j in range(col):
                print(matrix[i][j], end = " ")
        else:
            for j in range(col-1,-1,-1):
                print(matrix[i][j], end =" ")

r = int(input("Enter the number of rows:"))
c = int(input("Enter the number of columns:"))
matrix = []
for i in range(r):
    a = []
    for i in range(c):
        a.append(int(input()))
    matrix.append(a)
zigzag(matrix)




