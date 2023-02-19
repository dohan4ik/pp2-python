# Write a Python program to subtract five days from current date.
# Напишите программу на Python для вычитания пяти дней из текущей даты.
import datetime
today = datetime.date.today()
current_date = datetime.date.today() - datetime.timedelta(days = 5)
print(current_date)