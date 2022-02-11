people = int(input("mention the number of people: "))
if people >= 8:
    print("you have to wait for a table")
elif 0 < people < 8:
    print("your table is ready")
else:
    print("wrong input")
