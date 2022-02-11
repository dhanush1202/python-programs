a = float(input("give any number as 1st number: "))
b = float(input("give any number as 2nd number: "))
c = float(input("give any number as 3rd number: "))
def numbers():
    if a < b < c or c < b < a:
        print(b)
    elif b < a < c or c < a < b:
        print(a)
    elif a < c < b or b < c < a:
        print(c)


numbers()