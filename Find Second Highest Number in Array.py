arr=list(map(int,input().split()))

arr=list(set(arr))     # remove duplicates
arr.sort()

print("Second Highest:",arr[-2])
