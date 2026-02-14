def rev(n,r=0):
    if n==0:
        return r
    return rev(n//10,r*10+n%10)

n=int(input())
print("Palindrome" if rev(n)==n else "Not Palindrome")
