input = [int(i) for i in input().split()]
if len(input) <= 10 :
    input.sort()
    while input[0] == 0 :
        for i in range (len(input)):
            if input[0] == 0 :
                x = input[0]
                input[0] = input[i]
                input[i] = x
    for i in range (len(input)):
        print(input[i], end = '')
else :
    print("Error")                