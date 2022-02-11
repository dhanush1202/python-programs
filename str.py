n=input("enter the string: ")
a="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
b="1234567890"
l1=0
l2=0
for i in n:
    for j in a:
        if i==j:
            l1+=1
        
    for j in b:
        if i==j:
            l2+=1
        
print(l1)
print(l2)