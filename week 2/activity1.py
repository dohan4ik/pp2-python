"""
x = str(input())
i = 0
cnt = 0
def my_function(x):
    for i in x:
    #print(x[i])  
        if x[i] == "a" or x[i] == "e" or x[i] == "i" or x[i] == "o" or x[i] == "u":
            cnt += 1
        elif x[i] == "A" or x[i] == "E" or x[i] == "I" or x[i] == "O" or x[i] == "U":
            cnt += 1
        i += 1   
    return cnt 
my_function(x)
"""

x = input()
i = 0
cnt = 0
while i < len(x):
    #print(x[i])  
    if x[i] == "a" or x[i] == "e" or x[i] == "i" or x[i] == "o" or x[i] == "u":
        cnt += 1
    elif x[i] == "A" or x[i] == "E" or x[i] == "I" or x[i] == "O" or x[i] == "U":
        cnt += 1
    i += 1   
print(cnt)



#  a, e, i, o и 
