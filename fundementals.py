my_num = -5.6
my_string = 'Hello World!'
my_bool = False

print(my_bool)
print(my_string)
print(my_num)

if(my_num > 10):
    print('That is larger than 10')
else:
    print('That is not larger than 10')

if(my_num < 0 and my_bool == True):
    print('Negative and True')
elif(my_num >= 0 and my_bool == False):
    print('Positive and False')
elif(my_num > 100 or my_bool == True):
    print('Large or True')
else:
    print("I don't know")