day_in_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
def day_of_year(day,month,year) :
    day_of_years = 0
    if is_leap(year) : 
        day_in_month[2] = 29
    else : 
        day_in_month[2] = 28
        if month == 2 and day == 29 :
            return -1
        
    for i in range(1,month):
        day_of_years += day_in_month[i]
    day_of_years += day

    return day_of_years

def is_leap(year):
    return year%4 == 0 and (year%100 != 0 or year%400 == 0)

print(day_of_year(25))