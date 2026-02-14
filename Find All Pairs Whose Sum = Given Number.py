arr=list(map(int,input().split()))
target=int(input())

seen=set()
for i in arr:
    if target-i in seen:
        print(i, target-i)
    seen.add(i)
