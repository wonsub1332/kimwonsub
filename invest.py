year=0
balance=1000

while balance < 2000 :
    i= balance * 0.05
    balance= balance + i
    year=year + 1 

print("원금의 두배가 되는 기간(년) : ",year)
print("총액: ",balance)
