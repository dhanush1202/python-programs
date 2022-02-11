integers = []
integer = int(input("give an integer ('0' to exit): "))
while integer != 0:
    integers.append(integer)
    integer = int(input("give an integer ('0' to exit): "))
integers.sort()
for integer in integers:
    print(integer)