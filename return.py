def build_person(first_name, last_name):
    person = {'first': first_name, "last": last_name}
    return person


man = build_person('john', 'smith')
print(man)