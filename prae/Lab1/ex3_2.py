h1, m1, h2, m2 = [int(i) for i in input().split()]
count = 0
time = h2 - h1
min = m2 - m1	
if(h1 < 7 or h2 < 7 or h1 > 23 or h2 > 23 or time > 16 or time < 0 or (time == 0 and min < 0) or (h2 == 23 and m2 > 0) or (0 > (m1 or m2)) or ((m1 or m2) >= 60)):
    print("Error")  
else:
    if((min > 15 and time == 0) or (time <= 2 and time > 0) or (time == 3 and min == 0)):
        if(time <= 3 and time > 0 and min == 0):
            count = 10*(time)
        else:
            count = 10*(time + 1)
    elif(((time == 4 or time == 6) and min == 0) or (time <= 5 and time >= 3 and min != 0)):
        if(time <= 6 and time >= 4 and min == 0):
            count = 30 + 20*(time - 3)
        else:
            count = 30 + 20*(time - 2)
    elif((time == 6 and min > 0) or time > 6):
        count = 200
    print(count)