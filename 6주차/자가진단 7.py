#문자열 - 자가진단 7
#시와 분을 입력받아 출력예와 같은 형식으로 출력하는 프로그램을 작성하시오.
#(12시 이상인 경우 뒤에 PM을 출력하고, 그렇지 않은 경우에는 AM을 출력하되 13시 이상인 경우 시에서 12시를 뺀 값을 출력한다.)

hour, minute=map(int,input().split())

if hour>=12:
    ampm="PM"
else:
    ampm="AM"

if hour>12:
    hour=hour-12

if hour<10:
    print("0",end="")
print(hour,end=" : ")

if minute<10:
    print("0",end="")
print(minute,end=" ")

print(ampm)
