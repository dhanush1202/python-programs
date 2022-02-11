cities = {
    'hyderabad': {
        'country': 'India',
        'population': '68.1 lakhs',
        'fact': "hyderabad is the captial of southern India's Telangana state. A major centre for thr technology industry"
    },
    'mumbai': {
        'country': 'India',
        'population': '1.8 cr',
        'fact': "Mumbai is a densely populated city on India's west coast. A financial centre"
    },
    'Delhi': {
        'country': 'India',
        'population': '1.9 cr',
        'fact': "Delhi, India's capital territory, is a massive metropolitan area in the country's north."
    }
}
for k, v in cities.items():
    print(f"\ncity: {k}")
    for key, value in v.items():
        print(f"{key}: {value}")
