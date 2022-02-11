def shippingcharge(no):
    no = int(no)
    rate_first = 10.95
    rate_next = 2.95
    total_rate = rate_first + ((no - 1) * rate_next)
    print(f"total cost of shipping: {total_rate}")
shippingcharge(6)
