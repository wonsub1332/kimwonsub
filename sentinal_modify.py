n=0
sum=0
score=0

print("종료하려면 음수를 입력하시오")

while(score>=0):
    score = int(input("성적을 입력하시오: "))
    if score>0:
        sum=sum+score
    n += 1
    

if n==1:
    print("입력된 성적이 없습니다.")
elif sum==0 and n>1:
    print("성적의 평균은 0점 입니다.")
else:
    avg=sum/(n-1)
    print("%d개 과목 성적의 평균은 %0.2f입니다."%(n-1,avg))