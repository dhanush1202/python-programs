prompt = "\ntell me some thing i will repeat it back:"
prompt += "\nenter quit to exit"
message = ""
while prompt != 'quit':
    message = input(prompt)
    if message != "quit":
        print(message)
    else:
        break