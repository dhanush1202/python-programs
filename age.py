d=int(input("enter the date: "))
m=int(input("enter the month: "))
y=int(input("enter the year: "))
fd=int(input("enter the end date: "))
fm=int(input("enter the end month: "))
fy=int(input("enter the end year: "))
days=0
agey=fy-y-1
agem=0
for i in range(m,fm+12):
    agem+=1
aged=fd-d
if agem>12:
    agem-=12
    agey+=1
elif agem==12:
    agem-=1
    if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
        aged+=31
    elif m==4 or m==6 or m==9 or m==11:
        aged+=30
    else:
        aged+=28
print(agey,agem,aged)