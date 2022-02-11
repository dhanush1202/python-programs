def numbers():
    integer = int(input("give ant integer to give ordinal number: "))
    integers = {
        1: "first",
        2: "second",
        3: "third",
        4: "forth",
        5: "fifth",
        6: "sixth",
        7: "seventh",
        8: "eighth",
        9: "ninth",
        10: "tenth",
        11: "eleventh",
        12: "twelfth"
    }
    for key, value in integers.items():
        if integer == key:
            print(f"\nordinal number of {integer} is {value}")



numbers()