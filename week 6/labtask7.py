import re
camel = input() #Darkhan Tlepbergenov
snake = re.sub(r' ', '_', camel)
snake = snake.lower()
print(snake)