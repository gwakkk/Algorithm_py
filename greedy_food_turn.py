#https://programmers.co.kr/learn/courses/30/lessons/42891

import heapq

k = map(int,input("방송이 중단된 시간 : "))
food_times = list(map(int,input("섭취 소요 시간 : ").split()))
result = 0

if(k>sum(food_times)):
    return -1

q=[]

for i in range(len(food_times)):
    heapq.heappush(q,(food_times[i],i+1))

sum_value = 0
previous = 0
length = len(food_times)

while sum_value + ((q[0][0] - previous) * length) <= k:
    now = heapq.heappop(q)[0]
    sum_value += (now-previous) * length
    length -= 1
    previous = now

result = sorted(q, key=lambda x:x[1])
return result[(k-sum_value) % length][1]