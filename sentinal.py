n=0
sum=0
score=0

print("종료하려면 음수를 입력하시오")

while(1):
    score = int(input("성적을 입력하시오: "))
    if(score<0):
        break
    sum=sum+score
    n += 1
    

if n>0:
    avg=sum/n
else:
    avg=0

print("%d개 과목 성적의 평균은 %d입니다."%(n,avg))