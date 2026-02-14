n=int(input())
count,num=0,2

while count<n:
    for i in range(2,num):
        if num%i==0:
            break
    else:
        print(num,end=" ")
        count+=1
    num+=1
