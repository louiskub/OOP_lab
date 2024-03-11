#for row in range(10):
#    for col in range (10):
#       if row + col < 10:
#           print(' ', end = '')
#       else:
#           print('#', end = '')
#    print('#')
  
for i in range(10):
    print(' ' * (10 - i) + '#' * (i + 1))