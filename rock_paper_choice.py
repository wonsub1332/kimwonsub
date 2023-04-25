import random

li=["가위","바위","보"]
ans=input("가위 바위 보! : ")
ch=random.choice(li)

print("컴퓨터 : ",ch,  "|| 나 : ",ans)

if(ans==ch):
    print("비겼다")
elif((ans=="가위" and ch=="보")or(ans=="바위" and ch=="가위")or(ans=="보" and ch=="바위") ):
    print("이겼다")
else:
    print("졌다")
    