# Problem: E - Symmetrization - https://codeforces.com/gym/586960/problem/E

t = int(input())
for _ in range(t):

    n = int(input())
    
    Matrix = []
    for i in range(n):
        Matrix.append(input())
    

    operation = 0

    for row in range(n//2):
        for col in range(row, n - row - 1):
            
            zero_one_count = [0, 0]

            zero_one_count[int(Matrix[row][col])] += 1
            zero_one_count[int(Matrix[col][n - row - 1])] += 1
            zero_one_count[int(Matrix[n - row - 1][n - col - 1])] += 1
            zero_one_count[int(Matrix[n - col - 1][row])] += 1

            operation += min(zero_one_count)

    print(operation)