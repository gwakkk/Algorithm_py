n, m = map(int, input("N과 M을 입력 : ").split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    result = max(result,min(data))

print(result)
