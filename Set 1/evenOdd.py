def checkNumber(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

def main():
    number = int(input("\nEnter any number to check if is Even or Odd: "))
    result = checkNumber(number)
    print("\nThe number is {}\n".format(result))

main()