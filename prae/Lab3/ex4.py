def char_count(str) :
    count_str_dict = {}
    for i in str : count_str_dict[i] = str.count(i)
    return count_str_dict

str = 'language'
print(char_count(str))