for i in range (990, 1000):
    for j in range(900, 1000):
        x = str(i * j)
        for k in range (int(len(x)/2 + 1)):
            if(x[k] != x[len(x) - 1 - k]):
                break
            if(k >= len(x) - 1 - k):
                print(x)                           