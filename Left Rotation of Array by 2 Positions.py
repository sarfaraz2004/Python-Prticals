arr=list(map(int,input().split()))
k=2

arr=arr[k:]+arr[:k]
print(arr)
