a,b=map(int,input("N과 M을 입력 : ").split())
y=[]

for i in range(b):
    data=map(int,input().split())
    y.append(min(data))

print(max(y))
