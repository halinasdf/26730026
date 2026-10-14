#문자열 - 연습문제 7
#시와 분을 입력받아 출력예와 같은 형식으로 시간을 출력하는 프로그램을 작성하시오.

h=int(input("시를 입력하시오: "))
m=int(input("분을 입력하시오: "))

if h<10:
    print("0",end="")
print(h,end=":")

if m<10:
    print("0",end="")
print(m)
