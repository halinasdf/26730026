#문자열-연습문제1
#문자열 A를 입력받아 A의 모든 문자를 공백으로 분리하여 출력하는 프로그램을 작성하시오.

A = input("문자열 A를 입력하시오: ")

for i in range(len(A)):
    print(A[i], end=" ")
