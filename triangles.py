def lengths(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        print(True)
    else:
        print(False)



lengths(2, 5, 1)


def lengths1():
    a = input("give the length of first side: ")
    b = input("give the length of second side: ")
    c = input("give the length of third side: ")
    if a < b + c and b < a + c and c < a + b:
        print(True)
    else:
        print(False)



lengths1()
