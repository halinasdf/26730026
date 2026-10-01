#정수 N개를 입력받아 리스트에 저장한 후 모든 값의 평균을 출력하는 프로그램을 작성하시오.
N=int(input())
lst=[]

for i in range(N):
    temp=int(input())
    lst.append(temp)

print(int(sum(lst)/N))
