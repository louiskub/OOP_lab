h1, m1, h2, m2 = [int(i) for i in input().split()]
count = 0
time = 60*(h2 - h1) + m2 - m1 # Calculate parking time

# Calculate parking fees
if (h1 < 7 or h2 < 7) or (h1 > 23 or h2 > 23) or time < 0 or (h2 == 23 and m2 > 0) or (m1 < 0 or m2 < 0) or (m1 > 59 or m2 > 59) :
    print("Error")
else :
    if 15 < time <= 180 :
        count = 10*(time//60) if time % 60 == 0 else 10*(time//60 + 1)
    elif 181 <= time <= 360 :
        count = 30 + 20*(time//60 - 3) if time % 60 == 0 else 30 + 20*(time//60 - 2)
    elif time > 360 :
        count = 200
    print(count)