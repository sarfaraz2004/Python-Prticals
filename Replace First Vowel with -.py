s=input()
for i in s:
    if i.lower() in "aeiou":
        s=s.replace(i,"-",1)
        break
print(s)
