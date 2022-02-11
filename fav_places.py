fav_places = {
    'kane': ['texas', 'new york', 'washington DC'],
    'smith': ['sydney', 'london', 'hyderabad'],
    'rayudu': ['guntur', 'vijayawada', 'vishakapatanam']
}
for k, v in fav_places.items():
    print(f"\nfavourite places of {k} are:")
    for places in v:
        print(places)