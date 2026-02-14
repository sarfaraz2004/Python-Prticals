a,b=map(int,input().split())

x,y=a,b
while b:
    a,b=b,a%b

gcd=a
lcm=(x*y)//gcd
print("LCM:",lcm)
