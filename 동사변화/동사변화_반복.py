from ast import Break
# Data_type:Dictionary
index = 3
falar ={'eu':'falo', 'tu':'falas', 'ele':'fala', 'ela':'fala', 'você':'fala', 'nós':'falamos',
        'vós':'falais', 'eles':'falam', 'elas':'falam', 'vocês':'falam'}

print(falar['eu'])
print(falar.keys())
print(falar.values())

def sub_pronominal ():
    index = 3
    while index >=1:
        sub = input('Choose a pronominal to change FALAR:')
        if sub in falar:
            print(falar[sub])
        else:
            print('error')
        index -= 1
        if index == 0:
            return

def verbal_forms ():
    i = 3
    while i >= 1:
        verb = input('Enter one of verbal form of FALAR:')
        i -= 1
        for key, value in falar.items():
            if value == verb:
                print(key)
                if i == 0:
                    return

sub_pronominal()
verbal_forms()