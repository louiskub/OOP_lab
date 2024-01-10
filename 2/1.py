number = [int(e) for e in input().split() if e < 10]
if len(number)>10 : 
    print('err')
else :
    number = sorted(number)
    if number[0]==0 :
        for i in range(len(number)):
            if number[i]!=0 :
                number[0] = number[i]
                number[i] = 0
                break
    for e in number :
        print(e,end="")