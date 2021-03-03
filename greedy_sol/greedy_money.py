n = map(int, input("동전의 개수 : "))
coin_list = list(map(int, input().split()))
coin_list.sort()

a = 1
for item in coin_list:
    if(a < item):
        break
    else:
        a += item

print(a)
        

    