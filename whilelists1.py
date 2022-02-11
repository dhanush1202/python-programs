unconfirmed_user = ['john', 'smith', 'kane']
confirmed_user = []

while unconfirmed_user:
    verified_user = unconfirmed_user.pop()
    print(f"verifying user: {verified_user.title()}")
    confirmed_user.append(verified_user)