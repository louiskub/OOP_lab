string = input()
# string = 'kl12joeidksjqoi'
def only_english (string1) : 
    return ''.join([e for e in string1 if e.isalpha()])

print(only_english(string))
# string = ['s','o','p']
# string2 = ''.join(string)
# print(type(string2))