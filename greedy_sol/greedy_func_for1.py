a,b=map(int,input("N과 K를 입력 : ").split())
a,b =int(a),int(b)
count=0

while(a != 1):
    if(a % b != 0):
        a = a-1
        count +=1
    else:
        a //= b
        count +=1

print(count)