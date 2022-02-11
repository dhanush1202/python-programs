a = int(input("1st number: "))
b = int(input("2nd number: "))
c = int(input("3rd number: "))
d = int(input("4th number: "))
if a!=b!=c!=d:
        if a>b>c>d or a>d>c>b or d>a>c>b or b>a>c>d or b>d>c>a or d>b>c>a:
            second_smallest = c
        elif c>b>a>d or c>d>a>b or d>c>a>b or b>c>a>d or b>d>a>c or d>b>a>c:
            second_smallest = a
        elif a>c>b>d or a>d>b>c or d>a>b>c or c>a>b>d or c>d>b>a or d>c>b>a:
            second_smallest = b
        elif a>b>d>c or a>c>d>b or c>a>d>b or b>a>d>c or b>c>d>a or c>b>d>a:
            second_smallest = d
elif a==b and b!=c and b!=d:
    if a>c>d or d>c>a:
        second_smallest = c
    elif c>a>d or d>a>c:
        second_smallest = a
    elif a>d>c or c>d>a:
        second_smallest = d
elif a==b==c!=d:
    if a>d:
        second_smallest = a
    elif d>a:
        second_smallest = d
print(f"the second smallest number : {second_smallest}")
