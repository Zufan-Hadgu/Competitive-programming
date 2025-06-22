# Problem: Fox And Snake - https://codeforces.com/problemset/problem/510/A

n,m = map(int,input().split())
ans = []
for i in range(1,n+1):

    if i % 2 != 0:
        sign = '#' * m
        ans.append(sign)
    if i %2 == 0:
        if (i // 2)  % 2 != 0:
            sign = ('.'* (m -1)) + '#'
        else:
            sign = '#' + ('.' * (m-1))
        ans.append(sign)
print('\n'.join(ans))


    