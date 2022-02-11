favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
poll = ['jen', 'sarah']
for keys in favorite_languages.keys():
    if keys in poll:
        print(f"hi {keys}, thank you for responding!")
    else:
        print(f"hi {keys}, we invite you to take part in the poll!")