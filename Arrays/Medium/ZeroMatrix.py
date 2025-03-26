def markRow(a, i, m):
    for j in range(m):
        if a[i][j] != 0:
            a[i][j] = -1

def markCol(a, j, n):
    for i in range(n):
        if a[i][j] != 0:
            a[i][j] = -1

def zeroSetMatrix(a):
    n = len(a)      # Number of rows
    m = len(a[0])   # Number of columns

    for i in range(n):
        for j in range(m):
            if a[i][j] == 0:
                markRow(a, i, m)
                markCol(a, j, n)

    # Convert all -1s to 0s
    for i in range(n):
        for j in range(m):
            if a[i][j] == -1:
                a[i][j] = 0

# Example usage

zeroSetMatrix(matrix)
for row in matrix:
    print(row)
