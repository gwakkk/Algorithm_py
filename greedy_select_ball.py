a, b = map(int, input("N과 M을 입력 : ").split())
ball = list(map(int, input().split()))
count = 0

for i in range(len(ball)):
    for j in range(len(ball)):
        if(i>j):
            if(ball[i] != ball[j]):
                count += 1
            
print(count)