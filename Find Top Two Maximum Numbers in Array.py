arr=list(map(int,input().split()))
arr=list(set(arr))   # remove duplicates
arr.sort()

print("First Max:",arr[-1])
print("Second Max:",arr[-2])
