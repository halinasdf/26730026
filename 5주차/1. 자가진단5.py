#정수 n을 입력받고 n개의 정수를 입력받아 리스트에 저장한 후 리스트 전체를 출력하는 프로그램을 작성하시오.
n=int(input())
list=[]

for i in range(n):
    a=int(input())
    list.append(a)

print(list)
