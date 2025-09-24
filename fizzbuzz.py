def fizzbuzz(n1):
    if n1 % 3 == 0 and n1 % 5 == 0:
        return "FizzBuzz"
    elif n1 % 3 == 0:
        return "Fizz"
    elif n1 % 5 == 0:
        return "Buzz"
    else:
        return str(n1)


def validation(n1):
    if n1.isdigit():
        return True
    else:
        print("Invalid Input")
        return False


def main():
    while True:
        n1 = input("Enter a Number: ")
        if validation(n1) == True:
            n1 = int(n1)
            print(fizzbuzz(n1))
            user_input = input('Do you want to use the program again:(yes/no):  ').strip().lower()

            if user_input == "yes":
                print('Continuing program')
                continue
                
            else:
                print('Exiting program')
                break
        else:
            return False

if __name__ == "__main__":
    main()
