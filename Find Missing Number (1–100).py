arr=list(map(int,input().split()))
n=100
total=n*(n+1)//2
print("Missing number:",total-sum(arr))
