def add(a,b):
    if b==0:
        return a
    return add(a+1,b-1)

a=int(input())
b=int(input())
print(add(a,b))
