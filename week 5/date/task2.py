# Write a Python program to print yesterday, today, tomorrow.
# напишите программу для вывода вчера, сегодня , завтра
import datetime
today = datetime.date.today()
yesterday = datetime.date.today() - datetime.timedelta(days = 1)
tomorrow = datetime.date.today() + datetime.timedelta(days = 1)
print('Yesterday:', yesterday)
print('Today:', today)
print('Tomorrow:', tomorrow)