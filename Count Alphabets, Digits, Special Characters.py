s=input()
a=d=sp=0
for i in s:
    if i.isalpha():
        a+=1
    elif i.isdigit():
        d+=1
    else:
        sp+=1
print("Alphabets:",a)
print("Digits:",d)
print("Special characters:",sp)
