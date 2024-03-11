def add2list(lst1, lst2) :
    if(len(lst1) == len(lst2)) :
        return [lst1[i] + lst2[i] for i in range(len(lst1))]
    
x = [int(i) for i in input().split()]
y = [int(i) for i in input().split()]
print(add2list(x, y))    