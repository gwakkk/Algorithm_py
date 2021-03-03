data_a=list(map(int,input("숫자를 입력 : ")))

sum=0
product=1
for a in data_a:
    if(a == 0):
        sum += a
    elif(a == 1):
        sum += a
        product *= sum
    else:
        product *= a
print(product)