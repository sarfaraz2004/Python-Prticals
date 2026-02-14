n=int(input())
t,s=n,0
while t:
    s+=(t%10)**3
    t//=10
print("Armstrong" if s==n else "Not Armstrong")
