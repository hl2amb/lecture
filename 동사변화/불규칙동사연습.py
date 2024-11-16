import random

list_pronouns = ['eu', 'tu', 'ele', 'ela',
                 'nós', 'vós', 'elas','eles', 'você', 'vocês']

# list_irregular_verbs = ['ir', 'vir', 'estar', 'ser', 'ter', 'poder', 'ver']
list_irregular_verbs = ['ir', 'estar']

dic_ir = {'eu':'vou', 'tu':'vas', 'ele':'vai', 'ela':'vai', 'você':'vai',
               'nós':'vamos', 'vós':'vais', 'eles':'vão', 'elas':'vão', 'vocês':'vão'}

dic_estar = {'eu':'estou', 'tu':'estás', 'ele':'está', 'ela':'está', 'você':'está',
               'nós':'estamos', 'vós':'estais', 'eles':'estão', 'elas':'estão', 'vocês':'estão'}

choice_pronoun = random.choice(list_pronouns)
choice_verbs = random.choice(list_irregular_verbs)

verb = input('{} 동사를 {}에 맞게 변화시키시오: '.format(choice_verbs, choice_pronoun))

if choice_verbs == 'ir':
    for key, value in dic_ir.items():
        if key == choice_pronoun:
            while verb != dic_ir.get(choice_pronoun):
                    if verb == dic_ir.get(choice_pronoun):
                        print("Good Job!")
                    if verb != dic_ir.get(choice_pronoun):
                        agn = input("Wrong! Try again :")
                        continue # 반복문 만들기

elif choice_verbs == 'estar':
    for key, value in dic_estar.items():
        if key == choice_pronoun:
            if verb == dic_estar.get(choice_pronoun):
                print("Good Job!")
            if verb != dic_estar.get(choice_pronoun):
                agn = input("Wrong! Try again :")
                continue