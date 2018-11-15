def factorial(number):
    fact = 1

    while number > 0:
        fact *= number
        number -= 1
    
    return fact

def main():
    number = str(input("Enter a number: "))
    if number.isdigit():
        number = int(number)
        result = factorial(number)
        print(result)
    else:
        print('Wrong input...')

main()