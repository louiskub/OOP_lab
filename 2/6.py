x = [1,2,3,4,5]
y = [6,7,8,9,10]

def add2list(lst1,lst2) :
    ans = [ lst1[i]+lst2[i] for i in range(len(lst1)) ]
    return ans

print(add2list(x,y))