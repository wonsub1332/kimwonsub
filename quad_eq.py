import math
a=float(input("a :"))
b=float(input("b :"))
c=float(input("c :"))

if(a==0):
    print(-c/b)
else:
    d=(b*b-4*a*c)
    if(d==0):
        print("중근")
        print("x=" ,-b/(2*a))
    elif(d>0):
        print("다른 두 실근")
        print("x1=",-b+math.sqrt(d)/(2*a), "x2=",-b-math.sqrt(d)/(2*a))
    else:
        print("실근은 존재하지 않은다")

