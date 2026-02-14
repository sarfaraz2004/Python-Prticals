arr=list(map(int,input().split()))

freq={}
for i in arr:
    freq[i]=freq.get(i,0)+1

max_ele=max(freq,key=freq.get)
print("Highest frequency element:",max_ele)
