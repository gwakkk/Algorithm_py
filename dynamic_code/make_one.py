x = int(input("정수를 입력 : "))

# dp table reset
d = [0] * 30001

for i in range(2, x+1):
    # 현재수에서 1을 빼는 경우
    d[i] = d[i-1] + 1
    # 현재수가 2로 나누어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    # 현재수가 3으로 나누어지는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    # 5로 나누어 떨어지는 경우
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])