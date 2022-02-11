a = int(input("1st number: "))
b = int(input("2nd number: "))
c = int(input("3rd number: "))
d = int(input("4th number: "))
if a!=b!=c!=d:
        if a>b>c>d or a>d>c>b or d>a>c>b or b>a>c>d or b>d>c>a or d>b>c>a:
            print(f"the second smallest number : {c}")
        elif c>b>a>d or c>d>a>b or d>c>a>b or b>c>a>d or b>d>a>c or d>b>a>c:
            print(f"the second smallest number : {a}")
        elif a>c>b>d or a>d>b>c or d>a>b>c or c>a>b>d or c>d>b>a or d>c>b>a:
            print(f"the second smallest number : {b}")
        elif a>b>d>c or a>c>d>b or c>a>d>b or b>a>d>c or b>c>d>a or c>b>d>a:
            print(f"the second smallest number : {d}")
elif (a==b and b!=c and b!=d) or (a==c and c!=b and c!=d)or(a==d and d!=c and d!=b)\
        or(c==b and b!=a and b!=d)or(d==b and b!=c and b!=a)or(c==d and c!=b and c!=a):
    if a>c>d or d>c>a:
        print(f"the second smallest number : {c}")
    elif c>a>d or d>a>c:
        print(f"the second smallest number : {a}")
    elif a>d>c or c>d>a:
        print(f"the second smallest number : {d}")
elif (a==b==d and b!=c) or (a==b==c and b!=d) or (c==b==d and b!=a):
    if a>d:
        print(f"the second smallest number : {a}")
    elif d>a:
        print(f"the second smallest number : {d}")

else:
    print("second smallest number cannot be defined")