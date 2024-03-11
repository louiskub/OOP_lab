def only_english(string1) :
    return ''.join([i for i in string1 if i.isalpha()])

string1 = input()
print(only_english(string1))