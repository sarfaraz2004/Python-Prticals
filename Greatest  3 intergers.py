a,b,c=map(int,input().split())

if a>=b and a>=c:
    print("Greatest:",a)
elif b>=a and b>=c:
    print("Greatest:",b)
else:
    print("Greatest:",c)
