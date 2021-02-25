n = int(input("n을 입력 : "))

array = []
for i in range(n):
    array.append(int(input()))

array = sorted(array, reverse=True)

for i in array:
    print(i,end=' ')
    