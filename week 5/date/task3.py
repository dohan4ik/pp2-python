# Write a Python program to drop microseconds from datetime.
# Напишите программу на Python, чтобы убрать микросекунды из datetime.
import datetime
date_time = datetime.datetime.strptime(datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S"),"%Y-%m-%d %H:%M:%S")
current_time = date_time.time()
print(current_time)