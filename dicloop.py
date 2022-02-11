dic = {
    'first_name': 'dhanush',
    'last_name': 'gummadavalli',
    'age': '17',
    'city': 'hyderabad'
}

dic2 = {
    'first name': 'nikitha',
    'last name': 'gummadavalli',
    'age': '20',
    'city': 'hyderabad'

}
dic3 = {
    'first name': 'amar',
    'last name': 'gummadavalli',
    'age': '46',
    'city': 'hyderabad'

}
people = [dic.items(), dic2.items(), dic3.items()]
for items in people:
    for key, value in items:
        print('\n' + key + ':' + value)