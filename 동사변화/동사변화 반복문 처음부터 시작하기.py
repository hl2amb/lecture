import random
# import string

list_pronouns = ['eu', 'tu', 'ele', 'ela','nós', 'vós', 'elas','eles', 'você', 'vocês']


list_verbs = ['falar', 'amar', 'partir', 'lembrar', 'ceder', 'assistir']

firstChange = {'eu':'o', 'tu':'as', 'ele':'a', 'ela':'a', 'você':'a','nós':'amos',
               'vós':'ais', 'eles':'am', 'elas':'am', 'vocês':'am'}

secondChagne = {'eu':'o', 'tu':'es', 'ele':'e', 'ela':'e',  'você':'e',
                'nós':'emos','vós':'eis', 'eles':'em','elas':'em', 'vocês':'em'}

thirdChange = {'eu':'o', 'tu':'es', 'ele':'e', 'ela':'e',  'você':'e',
               'nós':'imos','vós':'is', 'eles':'em', 'elas':'em', 'vocês':'em'}


i = 0
while i < 3:

    choice_pronoun = random.choice(list_pronouns)
    choice_verbs = random.choice(list_verbs)

    verb = input('{} 동사를 {}에 맞게 변화시키시오: '.format(choice_verbs, choice_pronoun))
    root = choice_verbs[0:-2]

    if choice_verbs[-2:] == 'ar':
        for key, value in firstChange.items():
            if key == choice_pronoun:
                form = (root + firstChange.get(key))
                if form == verb:
                    print('correct')
                    i += 1
                if form != verb:
                    print("Incorrect")
                    while form != verb: # 부분 반복
                        verb = input('Incorrect! {} 동사를 {}에 맞게 변화시키시오: '.format(choice_verbs, choice_pronoun))
                        if form == verb:
                            print('correct')
                            i +=1

    elif choice_verbs[-2:] == 'er':
        for key, value in secondChagne.items():
            if key == choice_pronoun:
                form = (root + secondChagne.get(key))
                if form == verb:
                    print('correct')
                    i += 1
                if form != verb:
                    print("Incorrect")
                    while form != verb:
                        verb = input('{} 동사를 {}에 맞게 변화시키시오: '.format(choice_verbs, choice_pronoun))
                        i += 1

    elif choice_verbs[-2:] == 'ir':
        for key, value in thirdChange.items():
            if key == choice_pronoun:
                form = (root + thirdChange.get(key))
                if form == verb:
                    print('correct')
                    i += 1
                if form != verb:
                    print("Incorrect")
                    while form != verb:
                        verb = input('{} 동사를 {}에 맞게 변화시키시오: '.format(choice_verbs, choice_pronoun))
                        i += 1


