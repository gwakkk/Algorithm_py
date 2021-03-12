# 한번 계산된 결과를 저장하기 위한 리스트 초기화
d = [0] * 100

# 피보나치 함수를 재귀함수로 구현
def fibo(x):
    # 종료조건(1 or 2일때 1을 반환)
    if(x == 1 or x == 2):
        return 1
    # 이미 계산된 것이면 그대로 반환
    if d[x] != 0:
        return d[x]
    # 계산 안된것은 피보나치 결과 반환
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99)