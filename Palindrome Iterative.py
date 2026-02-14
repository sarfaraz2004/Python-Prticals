n=int(input())
t,rev=n,0
while t:
    rev=rev*10+t%10
    t//=10
print("Palindrome" if rev==n else "Not Palindrome")
