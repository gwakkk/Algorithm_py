n = int(input("N을 입력 : "))
array = [0] * 1000001

for i in input("가게에 존재하는 부품번호 입력 : ").split():
    array[int(i)] = 1

m = int(input("M을 입력 : "))
x = list(map(int,input("찾는 번호 입력 : ").split()))

for i in x:
    if array[i] == 1:
        print('yes',end='')
    else:
        print('no',end='')