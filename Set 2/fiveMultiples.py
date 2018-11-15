def fiveMultiples(number):
    for i in range (1, 6):
        print(str(number*i), end = ' ')

def main():
    number = str(input("Enter a number: "))
    if number.isdigit():
        number = int(number)
        fiveMultiples(number)
    else:
        print('Wrong input...')

main()