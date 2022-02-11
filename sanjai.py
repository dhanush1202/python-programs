n=int(input())
b=[120,30,220,50,320,90]
while n>0:
    
    if n>=50:
        d=int(input())
        n=n-b[d-1]
        if(n>0):
            print(n)
        else:
            print("insufficient bal")
            n=n+b[d-1]
    else:
        print("your shopping is over")
        break
    
