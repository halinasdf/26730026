#0이 입력될 때까지 정수를 입력받아 리스트에 저장한 후, 짝수번째(두 번째, 네 번째, 여섯 번째, ...) 값을 공백으로 구분하여 한 줄에 출력하는 프로그램을 작성하시오.
list=[]
while True:
    n=int(input("숫자를 입력하시오: "))
    if n ==0:
        break
    list.append(n)

for i in range(len(list)):
    if i % 2 ==1:
        print(list[i], end=" ")
