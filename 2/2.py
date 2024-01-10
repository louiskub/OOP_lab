x = ['abba', 'babana', 'ann']
c = 'a'
d = [0]*len(x)
for i in range(len(x)) :
    d[i] = x[i].count(c)
print(d)