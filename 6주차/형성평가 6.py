#문자열 - 형성평가 6
#문자열 하나를 입력받아 문자 사이사이에 마침표를 넣어 출력하는 프로그램을 작성하시오.

A=input("문자열을 하나 입력하시오: ")

for i in range(len(A)):
    print(A[i],end="")
    if i!=len(A)-1:
        print(".",end="")
