import random
# import string

list_pronouns = ['eu', 'tu', 'ele', 'ela','nós', 'vós', 'elas','eles', 'você', 'vocês']

list_verbs = ['falar', 'amar',  'lembrar',]

list_tense = ['현재', '반과거']

# list_verbs = ['falar', 'amar', 'partir', 'lembrar', 'ceder', 'assistir']
firstChange_present = {'eu':'o', 'tu':'as', 'ele':'a', 'ela':'a', 'você':'a','nós':'amos',
               'vós':'ais', 'eles':'am', 'elas':'am', 'vocês':'am'}

firstChange_imperfeito = {'eu':'ava', 'tu':'avas', 'ele':'ava', 'ela':'ava', 'você':'ava','nós':'avamos',
               'vós':'avais', 'eles':'avam', 'elas':'vam', 'vocês':'avam'}

# secondChagne = {'eu':'o', 'tu':'es', 'ele':'e', 'ela':'e',  'você':'e',
#                 'nós':'emos','vós':'eis', 'eles':'em','elas':'em', 'vocês':'em'}
#
# thirdChange = {'eu':'o', 'tu':'es', 'ele':'e', 'ela':'e',  'você':'e',
#                'nós':'imos','vós':'is', 'eles':'em', 'elas':'em', 'vocês':'em'}


choice_pronoun = random.choice(list_pronouns)
choice_verbs = random.choice(list_verbs)
choice_tense = random.choice(list_tense)

root = choice_verbs[0:-2]

verb = input('{} 동사를 {}에 맞게 {} 시제로 변화시키시오: '.format(choice_verbs, choice_pronoun, choice_tense))

if choice_verbs[-2:] == 'ar' and choice_tense == '현재':
    for key, value in firstChange_present.items():
        if key == choice_pronoun:
            form = (root + firstChange_present.get(key))
            if form == verb:
                print('correct')
            while form != verb:
                print("Correct form is '{}'.Try again!".format(form.upper()))
                verb = input('{} 동사를 {}에 맞게 {} 시제로 변화시키시오: '.format(choice_verbs, choice_pronoun, choice_tense))
                if form == verb:
                    print("Correct!")

elif choice_verbs[-2:] == 'ar' and choice_tense == '반과거':
    for key, value in firstChange_imperfeito.items():
        if key == choice_pronoun:
            form = (root + firstChange_imperfeito.get(key))
            if form == verb:
                print('correct')
            while form != verb:
                print("Correct form is '{}'.Try again!".format(form.upper()))
                verb = input('{} 동사를 {}에 맞게 {} 시제로 변화시키시오: '.format(choice_verbs, choice_pronoun, choice_tense))
                if form == verb:
                    print("Correct!")

# elif choice_verbs[-2:] == 'er':
#     root = choice_verbs[0:-2]
#     for key, value in secondChagne.items():
#         if key == choice_pronoun:
#             form = (root + secondChagne.get(key))
#             if form == verb:
#                 print('correct')
#             if form != verb:
#                 print("Correct form is '{}'.Try again!".format(form.upper()))
#                 while form != verb:
#                     verb = input('{} 동사를 {}에 맞게 변화시키시오: '.format(choice_verbs, choice_pronoun))
#                 # break
#
# elif choice_verbs[-2:] == 'ir':
#     root = choice_verbs[0:-2]
#     for key, value in thirdChange.items():
#         if key == choice_pronoun:
#             form = (root + thirdChange.get(key))
#             if form == verb:
#                 print('correct')
#             if form != verb:
#                 print("Correct form is '{}'.Try again!".format(form.upper()))
#                 while form != verb:
#                     verb = input('{} 동사를 {}에 맞게 변화시키시오: '.format(choice_verbs, choice_pronoun))
#                 # break

