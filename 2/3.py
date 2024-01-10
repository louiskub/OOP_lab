x = [ [1, -3, 2], [-8, 5], [-1, -4, -3] ]
ans = [[num for num in i if num >= 0] for i in x]
print(ans)