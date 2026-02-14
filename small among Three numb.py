a,b,c=map(int,input().split())

if a<=b and a<=c:
    print("Smallest:",a)
elif b<=a and b<=c:
    print("Smallest:",b)
else:
    print("Smallest:",c)
