#문자열 - 형성평가 7
#문자열 하나를 입력받아 거꾸로 순회하여 출력하고 다시 원래대로 출력하는 프로그램을 작성하시오.

A=input("문자열을 하나 입력하시오: ")

for i in range(len(A)-1,-1,-1):
    print(A[i],end="")
print()

for i in range(len(A)):
    print(A[i],end="")
