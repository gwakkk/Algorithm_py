n= int(input("N을 입력 : "))
x, y = 1, 1
nx, ny = 1, 1
a = input().split()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1 ,1]

mov_types = ['L', 'R', 'U', 'D']

for plan in a:
    for i in range(len(mov_types)):
        if plan == mov_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue

        x, y = nx, ny

print(x, y)