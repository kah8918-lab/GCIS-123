def  calc(n1,n2, choise ):
    if choise.lower() == 'addition':
        calc = n1+n2
        return calc
    elif choise.lower() == 'subtraction':
        calc = n1-n2
        return calc
    elif choise.lower() == 'multiplication':
        calc = n1*n2
        return calc
    elif choise.lower() == 'division':

        if n2 == 0:
            return 'Error: Division by zero is not allowed.'
        else:
            calc = n1/n2
            return calc
    
    else:
        return 'Invalid choise'
    
def main():


    
    while True:
        
        valid_choises = ['addition', 'subtraction', 'multiplication', 'division']
        
        choise = input('Enter the operation you want to perform (addition, subtraction, multiplication, division) or write done to stop using calculator: ')

        if choise.lower() == 'done':
            print('Goodbye!')
            break

        if choise.lower() not in valid_choises:
            print('Invalid choise, please try again.')
            continue
        
    
    
    
        try:
            n1 = float(input('enter the first value: '))
            n2 = float(input("enter the second value: "))

        except ValueError:
            print('Invalid input, please enter numeric values.')
            continue

        x = calc (n1,n2, choise)
        print(x)
main()
