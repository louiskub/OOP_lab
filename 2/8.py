day_in_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    return year%4 == 0 and (year%100 != 0 or year%400 == 0)

def day_in_year (year) :
    return 366 if is_leap(year) else 365

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

def date_diff (date1 , date2) :
    day1 , month1 ,year1 = map(int , date1.split('-'))
    day2 , month2 ,year2 = map(int , date2.split('-'))

    if year1 == year2:
        return day_of_year(day2,month2,year2) - day_of_year(day1,month1,year1)

    ans = day_in_year(year1) - day_of_year(day1,month1,year1)
    for i in range(year1+1,year2) :
        ans += day_in_year(i)

    ans += day_of_year(day2,month2,year2)
    return ans+1

data1 = input('dd-mm-yyyy : ')
data2 = input('dd-mm-yyyy : ')
print( date_diff(data1 , data2) )