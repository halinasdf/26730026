#0이 입력될 때까지 정수를 입력받아 리스트에 저장한 후 차례대로 출력하는 프로그램을 작성하시오.
list=[]
while True:
    n=int(input())
    if n ==0:
        break
    list.append(n)

for n in list:
    print(n)
