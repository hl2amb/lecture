firstChange = {'eu':'o', 'tu':'as', 'ele':'a', 'nós':'amos','vós':'ais', 'eles':'am'}
secondChagne = {'eu':'o', 'tu':'es', 'ele':'e', 'nós':'emos','vós':'eis', 'eles':'em'}

thirdChange = {'eu':'o', 'tu':'es', 'ele':'e', 'nós':'imos','vós':'is', 'eles':'em'}

verb = input("Enter a verb: ")
pronoun = input("Enter a personal pronoun: ")
root = verb[0:-2]


if verb[-2:] == 'ar':
    for key, value in firstChange.items():
        if pronoun == key:
            print(pronoun, root+firstChange.get(key))
elif verb[-2:] == 'er':
    for key, value in secondChagne.items():
        if pronoun == key:
            print(pronoun, root + secondChagne.get(key))
elif verb[-2:] == 'ir':
    for key, value in thirdChange.items():
        if pronoun == key:
            print(pronoun, root + thirdChange.get(key))
else:
    print("Input error.")

