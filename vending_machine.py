price=int(input("물건 번호을 입력하시오 : "))
i1000=int(input("1000원 지폐 개수 :"))
i500=int(input("500원 지폐 개수 :"))
i100=int(input("100원 지폐 개수 :"))

money= i1000*1000+i500*500+i100*100

exc=money-price

out500=exc//500
exc=exc%500

out100=exc//100
exc=exc%100

out50=exc//50
exc=exc%50

out10=exc//10
exc=exc%10



print("=====거스름돈=======")
print("500원 %d개 / 100원 %d개 /50원 %d개 / 10원 %d개"%(out500,out100,out50,out10))
