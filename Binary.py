n=input()
flag=1
for i in n:
    if i not in "01":
        flag=0
        break
print("Binary" if flag else "Not Binary")
