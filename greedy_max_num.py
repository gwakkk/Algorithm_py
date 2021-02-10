n,m,k = map(int, input("N, M, K를 입력 : ").split())
data = list(map(int, input("N개의 자연수 입력 : ").split()))

data.sort()
sum = 0
count = 0
for i in range(m):
    if count >= k:
        sum += data[-2]
        count = 1
        
    else:
        sum += data[-1]
        count +=1
print(sum)