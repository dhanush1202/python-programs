cost_first = 10.95
subsequent = 2.95
def cost(number):
    total_cost = cost_first + ((number - 1) * subsequent)
    print(f"the total cost of shipping material of {number} items is {total_cost}")
cost(number= 6)