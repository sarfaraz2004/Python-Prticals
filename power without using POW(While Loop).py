a,b=map(int,input().split())
p=1
while b>0:
    p*=a
    b-=1
print(p)
