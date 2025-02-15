# Problem: D - Bomb Detection Validation - https://codeforces.com/gym/586960/problem/D

n, m = map(int, input().split())
matrix = []

 
for k in range(n):
    row = list(input().strip())   
    matrix.append(row)

 
directions = [
    [-1, -1], [-1, 0], [-1, 1],
    [0, -1],         [0, 1],
    [1, -1], [1, 0], [1, 1]
]

valid = True   
for i in range(n):
    for j in range(m):
        if matrix[i][j].isdigit():   
            expected_bombs = int(matrix[i][j])
            bomb_count = 0

             
            for d in directions:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < n and 0 <= nj < m and matrix[ni][nj] == '*':
                    bomb_count += 1
            
            if bomb_count != expected_bombs:
                valid = False
                break   
        
        elif matrix[i][j] == '.':  
            for d in directions:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < n and 0 <= nj < m and matrix[ni][nj] == '*':
                    valid = False
                    break   
    if not valid:
        break   
 
print("YES" if valid else "NO")
