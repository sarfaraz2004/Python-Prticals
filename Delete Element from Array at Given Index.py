arr=list(map(int,input().split()))
index=int(input())

if index < len(arr):
    arr.pop(index)
print(arr)
