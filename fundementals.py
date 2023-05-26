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

my_strings = ['This is the first string','This is the second string','This is the third string']
my_nums = [1,2,3,4,5,6]

for string in my_strings:
    print(string)

for num in my_nums:
    print(f'Look at this number: {num}')

def static_greeting():
    print('Hello Alex')

static_greeting()

def dynamic_greeting(to_greet):
    print('Hello', to_greet)

dynamic_greeting('Bob')
dynamic_greeting('Alice')
dynamic_greeting('Rob')