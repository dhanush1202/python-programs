jimmy = {
    'animal': 'dog',
    'owner': 'jonny'

}
john = {
    'animal': 'cat',
    'owner': 'sins'
}
marry = {
    'animal': 'snake',
    'owner': 'danny'
}
peter = {
    'animal': 'horse',
    'owner': 'daniel'
}
john = john.items()
peter = peter.items()
marry = marry.items()
jimmy = jimmy.items()
pets = [jimmy, john, marry, peter]

for items in pets:
    print('\n')

    for keys, values in items:

        print(f"{keys}: {values}")
