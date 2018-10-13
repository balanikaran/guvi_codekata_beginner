def checkNumber(number):
    if number == 0:
        return "Zero"
    elif number < 0:
        return "Negative"
    elif number > 0:
        return "Positive"

def main():
    number  = int(input("\nEnter any number to check if it is positive/negative/zero: "))
    result = checkNumber(number)
    print("\nThe number is {}\n".format(result))

main()