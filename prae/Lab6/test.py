from datetime import datetime, time
from datetime import timedelta

## 1 ##
current_datetime = datetime.now()
print(current_datetime)
print('')

## 2 ## 
formatted_date = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
print(formatted_date)
print('')

## 3 ## 
date_string = '2024-01-17 12:30:00'
parsed_date = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
print(parsed_date)
print('') 

## 4 ##
future_date = current_datetime + timedelta(days = 7)
time_difference = future_date - current_datetime
print(f"Future Date: {future_date}")
print(f"Time Difference: {time_difference}")
print('')

## 5 ##
specific_date = datetime(2023, 5, 15, 14, 30)
print(specific_date)
print('')

## 6 ##
yesterday = current_datetime - timedelta(days = 1)
tomorrow = current_datetime + timedelta(days = 1)
print(f"Yesterday: {yesterday}")
print(f"Tomorrow: {tomorrow}")
print('')

## 7 ##
current_time = datetime.now().time()
print(current_time)

## 8 ##
formatted_time = datetime.now().strftime('%H:%M:%S')
print(formatted_time)

## 9 ##
# Or create a specific time
specific_time = time(0, 0, 0)
print(specific_time)