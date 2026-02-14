def sumd(n):
    if n==0:
        return 0
    return n%10 + sumd(n//10)

n=int(input())
print("Sum of digits:",sumd(n))
