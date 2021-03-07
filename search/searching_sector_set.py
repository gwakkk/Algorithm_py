n = int(input("N을 입력 : "))

array = set(map(int,input("전체 부품번호 입력 : ").split()))

m = int(input("확인 요청 부품 입력 : "))
x = list(map(int, input("검색 부품번호 입력 : ").split()))

for i in x:
    if i in array:
        print('yes', end= ' ')
    else:
        print('no', end = ' ')