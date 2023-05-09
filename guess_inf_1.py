import random
target=random.randint(1,100)
ans=0
tries=0
print("숫자 게임에 오신 것을 환영합니다.")
print("1~100 사이의 숫자를 맞춰 보세요")

while True:
    ans=int(input("숫자를 입력하시오 :"))
    tries +=1
    if(target==ans):
        print("정답을 맞췄습니다. 시도횟수 %d"%tries )
        break
    elif(target>ans):
        print("정답보다 작습니다.")
    else:
        print("정답보다 큽니다.")