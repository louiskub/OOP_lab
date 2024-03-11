def count_char_in_string(x, c) :
    return [i.count(c) for i in x] 
    
x = input().split()
print(count_char_in_string(x, 'a')) 