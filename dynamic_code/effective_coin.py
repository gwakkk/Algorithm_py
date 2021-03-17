n, m = map(int(input("n과 m을 입력 : ").split()))

array = []
for i in range():
    array.append(int(input("화폐정보를 입력 : ")))

d = [10001] * (m + 1)

d[0] = 0
for i in range(n):
    for j in range(array[i], m+1):
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j-array[i]+1])

if d[m] == 10001:
    print(-1)
else:
    print(d[m])