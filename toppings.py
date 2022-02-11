toppings = "\nhelp us to some toppings to pizza(quit to exit): "
msg = ""
while toppings != 'quit':
    msg = input(toppings)
    print(f" toppings to be added: {msg}")
    if msg == "quit":
        break
