n,k=map(int, input("N과 K를 입력 :").split())
count=0

while True:
    if n < k:
        break
    target = (n // k) * k
    count += (n-target)
    n = target
    count += 1
    n //= k

count += (n-1)
print(count)