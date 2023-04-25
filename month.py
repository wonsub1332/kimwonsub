month=int(input("월을 입력하시오 : "))
sortM=[2,4,6,9,11]

if(month in sortM):
    if(month==2):
        print(month,"월의 날수는 28일")
    else:
        print(month,"월의 날수는 30일")
else :
    print(month,"월의 날수는 31일")
