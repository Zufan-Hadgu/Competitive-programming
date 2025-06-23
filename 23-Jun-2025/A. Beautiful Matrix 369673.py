# Problem: A. Beautiful Matrix - https://codeforces.com/problemset/problem/263/A

row1 = list(map(int,input().split()))
row2 = list(map(int,input().split()))
row3 = list(map(int,input().split()))
row4 = list(map(int,input().split()))
row5 = list(map(int,input().split()))


matrix = [row1,row2,row3,row4,row5]

indexes = []
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            indexes = [i+1,j+1]
            break

miniMove = abs(indexes[0] - 3 ) + abs(indexes[1] - 3)

print(miniMove)

