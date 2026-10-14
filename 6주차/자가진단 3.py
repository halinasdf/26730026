#문자열 - 자가진단 3
#한 줄에 공백으로 구분된 두 개의 단어로 이루어진 문자열을 입력받아, 두 번째 단어를 먼저 출력한 후 공백으로 구분하여
#첫 번째 단어와 두 번째 단어를 붙여서 출력하는 프로그램을 작성하시오

A=input("한 줄에 공백으로 구분된 두 개의 단어로 이루어진 문자열을 입력하시오: ")

word1=""
word2=""
blank=0

for i in range(len(A)):
    if A[i]==" ":
        blank=i
        break

for i in range(blank):
    word1=word1+A[i]

for i in range(blank+1,len(A)):
    word2=word2+A[i]

print(word2, end=" ")
print(word1+word2)
