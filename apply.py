state=input("사과의 상태를 입력하시오(신선,시들): ")

if(state=="신선"):
    price=int(input("사과 1개의 가격을 입력하시오: "))
    if(price<1000):
        print("개당 1000원 미만이므로 10개를 산다.")
    else:
        print("개당 1000원 이상이므로 5개를 산다.")
else:
    print("사과를 사지 않는다.")
