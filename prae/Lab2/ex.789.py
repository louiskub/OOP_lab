d = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year) :
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
        
def day_of_year(day, month, year) :
    count = 0
    if is_leap(year) :
        d[1] = 29
    for i in range(month-1) :
        count += d[i]
    d[1] = 28
    return count + day

def day_in_year(year) :
    return 366 if is_leap(year) else 365
        
def date_diff(date1, date2) :
    d1, m1, y1 = [int(i) for i in date1.split('-')]
    d2, m2, y2 = [int(i) for i in date2.split('-')]
    if (m1 < 1 or m1 > 12) or (m2 < 1 or m2 > 12) or (d1 < 1 or d2 < 1) or (d1 > 29 and is_leap(y1)) or \
    (d2 > 29 and is_leap(y2)) or (d1 > d[m1-1] and ~is_leap(y1)) or (d2 > d[m2-1] and ~is_leap(y2)) :
        return -1
    else :
        count = day_of_year(d2, m2, y2) - day_of_year(d1, m1, y1) + 1
        for i in range(y1, y2) :
            count += day_in_year(i)
        return count 
  
date1, date2 = input().split()
print(date_diff(date1, date2))