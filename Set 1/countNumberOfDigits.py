def countDigits(number):
    digits = 0
    while number != 0:
        number //= 10
        digits += 1
    return digits

def main():
    number = int(input("Enter any number: "))
    result = countDigits(number)
    print("Number of digits = {}".format(result))

main()