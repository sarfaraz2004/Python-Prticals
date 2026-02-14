arr=list(map(int,input().split()))
x=int(input())

if x in arr:
    arr.remove(x)
print(arr)
