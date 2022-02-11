def city_country(city, country):
    cc = city + ", " + country
    return cc.title()



cc1 = city_country('"santiago', 'chile"')
print(cc1)