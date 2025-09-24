#for loop
'''

for i in range(1,11): #this will print numbers from 1 to 10
    print(i)
print('The loop has finished') #this will print when the for loop has finished




vowels = 'aeiou'
string= 'This is a test string'
vowel_count = 0 
for char in string: 
    if char in vowels: 
        print(char)
        vowel_count += 1
print('There are', vowel_count, 'vowels in the string') 


'''

user_input= input('Enter a number: ')
system_counter_even= 0
system_counter_odd= 0
for i in user_input:
    if int(i) % 2 == 0:
        system_counter_even += 1
        print(i, 'is even')
    else:
        int(i) % 2 != 0
        system_counter_odd += 1
        print(i, 'is odd')
print('There are', system_counter_even, 'even numbers in the input')
print('There are', system_counter_odd, 'odd numbers in the input')


'''


#challenges

#1 Counting to 100
for x in range (101):
    print(x)

#2 Even or odd finder
user_input= input('Enter a number: ')
system_counter_even= 0
system_counter_odd= 0
for i in user_input:
    if int(i) % 2 == 0:
        system_counter_even += 1
        print(i, 'is even')
    else:
        int(i) % 2 != 0
        system_counter_odd += 1
        print(i, 'is odd')
print('There are', system_counter_even, 'even numbers in the input')
print('There are', system_counter_odd, 'odd numbers in the input')


 '''
 #create a calculator program

num1= float(input('Enter your first number: '))
num2= float(input('Enter your second number: '))
operation= input('Enter the operation you would like to perform (+, -, *, /): ')
if operation == '+':
    print(num1 + num2)
elif operation == '-':
    print(num1 - num2)
elif operation == '*':
    print(num1 * num2)
elif operation == '/':
    if num2 != 0:
        print(num1 / num2)
    else:
        print('Error: Division by zero is not allowed.')
else:
    print('Invalid operation. Please enter one of +, -, *, or /.')
    

