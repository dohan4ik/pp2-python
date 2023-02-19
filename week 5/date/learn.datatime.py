import datetime
# print(datetime.datetime.now()) выведет нынежнее число и время

# print(datetime.date.today())  выведет дату

# date_time = datetime.datetime.now() 
# current_time = date_time.time()  достаем только време 
#print(current_time)                    

# print(datetime.time(12, 12, 12))  указываем время которое хотим

# print(datetime.datetime(2022, 7, 22))  выводит указыную дату если не указать време выведет время 00:00:00

# print(datetime.datetime(2022, 7, 22, 12, 30 , 45))  выводит указыну. дату и время

# td_object = datetime.timedelta(days = 5, seconds = 5, microseconds = 4, milliseconds = 1, minutes = 10, hours = 2, weeks = 5)
# print(td_object)  выведет 40 дней и время 2:20:05:001004
# timedelta суммирует все

# date = datetime.date.today() - datetime.timedelta(days = 7)
# print(date)

# today = datetime.date.today()
# next_date = datetime.date.today() + datetime.timedelta(days = 7)
# print('Сегодны > через неделю', today > next_date)  выведет фолс потаму что через неделю больше чем этот день

# now = datetime.time(11, 10,12)
# next_hourse = datetime.time(13, 14, 11)
# print('сейчас < позже', now < next_hourse)\

# date = "06/05/22 12:06:58"
# date_obj = datetime.datetime.strptime(date, "%m/%d/%y %H:%M:%S")
# print(date_obj)

