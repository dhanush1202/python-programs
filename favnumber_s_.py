favourite_numb = {
    'bill': [5, 4, 6],
    'gates': [7, 3, 1],
    'steve': [3, 6, 9],
    'jobs': [2, 0, 5],
    'elon mask': [9, 6, 12]
}
for k, v in favourite_numb.items():
    print(f"\nfavourite numbers of {k} are:")
    for numbers in v:
        print(numbers)
