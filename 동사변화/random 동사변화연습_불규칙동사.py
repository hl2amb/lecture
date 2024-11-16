import random
# import string

list_pronouns = ['eu', 'tu', 'ele', 'ela',
                 'nós', 'vós', 'elas','eles', 'você', 'vocês']

list_verbs = ['falar', 'comer', 'partir', 'lembrar', 'ceder', 'assistir','ir',
              'vir', 'estar', 'ser', 'ter', 'poder', 'ver']

list_irregular_verbs = ['ir', 'vir', 'estar', 'ser', 'ter', 'poder', 'ver']

firstChange = {'eu':'o', 'tu':'as', 'ele':'a', 'ela':'a', 'você':'a',
               'nós':'amos', 'vós':'ais', 'eles':'am', 'elas':'am', 'vocês':'am'}

secondChagne = {'eu':'o', 'tu':'es', 'ele':'e', 'ela':'e',  'você':'e',
                'nós':'emos','vós':'eis', 'eles':'em','elas':'em', 'vocês':'em'}

thirdChange = {'eu':'o', 'tu':'es', 'ele':'e', 'ela':'e',  'você':'e',
               'nós':'imos','vós':'is', 'eles':'em', 'elas':'em', 'vocês':'em'}


choice_pronoun = random.choice(list_pronouns)
choice_verbs = random.choice(list_verbs)

verb = input('{} 동사를 {}에 맞게 변화시키시오: '.format(choice_verbs, choice_pronoun))

if choice_verbs in list_irregular_verbs:
    print("It's irregular verbs.")


elif choice_verbs[-2:] == 'ar':
    root = choice_verbs[0:-2]
    for key, value in firstChange.items():
        if key == choice_pronoun:
            form = (root + firstChange.get(key))
            if form == verb:
                print('correct')
            if form != verb:
                print("Correct form is '{}'.Try again!".format(form.upper()))
                # break

elif choice_verbs[-2:] == 'er':
    root = choice_verbs[0:-2]
    for key, value in secondChagne.items():
        if key == choice_pronoun:
            form = (root + secondChagne.get(key))
            if form == verb:
                print('correct')
            if form != verb:
                print("Correct form is '{}'.Try again!".format(form.upper()))
                # break

elif choice_verbs[-2:] == 'ir':
    root = choice_verbs[0:-2]
    for key, value in thirdChange.items():
        if key == choice_pronoun:
            form = (root + thirdChange.get(key))
            if form == verb:
                print('correct')
            if form != verb:
                print("Correct form is '{}'.Try again!".format(form.upper()))
                # break

