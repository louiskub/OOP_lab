text = input()
small = big = 0
for i in range(len(text)):
    if(text[i] >= 'a' and text[i] <= 'z'):
        small += 1
    elif(text[i] >= 'A' and text[i] <= 'Z'):
        big += 1
print(str(small) + "\n" + str(big))