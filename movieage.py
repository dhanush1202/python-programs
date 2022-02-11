age = input("\nage of the person entering: ")

msg = ""
while age != "":
    msg = age
    if int(msg) < 3:
        ticket_cost = 0
    elif 3 <= int(msg) <= 12:
        ticket_cost = 10
    elif int(msg) > 12:
        ticket_cost = 15
    print(f"ticket cost: {ticket_cost}")
    age = input("enter the age of person: ")
    if age == "":
        break
