favourite_numb = {
    'bill': 5,
    'gates': 7,
    'steve': 3,
    'jobs': 2,
    'elon mask': 9
}
person = input("name of the person to give favourite number: ")
if person.lower() == "bill":
    favourite_number = favourite_numb['bill']
elif person.lower() == "gates":
    favourite_number = favourite_numb['gates']
elif person.lower() == "steve":
    favourite_number = favourite_numb['steve']
elif person.lower() == "jobs":
    favourite_number = favourite_numb['jobs']
elif person.lower() == "elon mask":
    favourite_number = favourite_numb['elon mask']
else:
    favourite_number = 'not given'
print(f"favourite number of {person} is {favourite_number}")