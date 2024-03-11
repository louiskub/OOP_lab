def delete_minus(x) :
    return [[i for i in sub if i >= 0] for sub in x]

x = [int(i) for i in input().split()]
print(delete_minus(x))