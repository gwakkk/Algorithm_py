n = int(input("학생 수를 입력 : "))

array = []

for i in range(n):
    input_data = input().split()
    array.append((input_data[0],int(input_data[1])))2

array = sorted(array, key=lambda student: student[1])

for student in array:
    print(student[0],end=' ')