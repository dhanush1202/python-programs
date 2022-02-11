integer = []
integers = input("give any integer(blank to exit): ")
while integers != '':
    integer.append(integers)
    integers = input("give any integer(blank to exit): ")
integer.sort()
for integers in integer:
    print(integers)
