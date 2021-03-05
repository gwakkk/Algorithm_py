def binary_search(array,target,start,end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
             end=mid-1
        else:
            start = mid+1
        return None

n=int(input("N을 입력 : "))
array=list(map(int,input("전체 부품번호 입력 : ").split()))
array.sort()

m=int(input("M을 입력 : "))
x=list(map(int,input("필요 부품번호 입력 : ").split()))

for i in x:
    result = binary_search(array,i,0,n-1)
    if result != None:
        print('yes', end='')
    else:
        print('no',end='')