idList=["로미오","짜장","흥부"]
pwList=["줄리엣","짬뽕","놀부"]
id=input("아이디를 입력하시오: ")


if(id in idList):
    pw=input("패스워드를 입력하시오: ")
    if(pw in pwList):
        print(id,"님 환영합니다.")
    else:
        print("잘못된 패스워드입니다.")
else:
    print("알 수 없는 사용자입니다.")