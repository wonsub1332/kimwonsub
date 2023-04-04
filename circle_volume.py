import math
math.pi

r= int(input("반지름 :"))

v= 4/3*math.pi * r**3

print("반지름 ",r,"인 원의 부피는",v)

print("반지름 %d인 원의 부피는 %f"%(r,v))