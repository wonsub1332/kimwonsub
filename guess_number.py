import random
target=random.randint(1,10)

print("숫자 게임에 오신 것을 환영합니다.")
ans=int(input("1~10 사이의 숫자를 맞춰 보세요 : "))

if(target==ans):
    print("정답을 맞췄습니다.")
elif(target>ans):
    print("정답보다 작습니다.")
else:
    print("정답보다 큽니다.")
print("게임 종료")