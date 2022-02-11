basic_cost = 4.00
extra_charges = 0.25
charge_permeter = 0.0017857142857142857
def distance(km):
    m = km / 1000
    total_cost = basic_cost + (m * charge_permeter)
    print(f"\n\ntotal cost according to jurisdiction is {total_cost}")
distance(km=5)