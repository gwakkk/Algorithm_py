#count 3 in all times under Nhour

n = int(input("정수 N을 입력 : "))
count = 0

for x in range(n+1):
    for i in range(60):
        for j in range(60):
            if('3' in str(x)+str(i)+str(j)):
                count += 1

print(count)

