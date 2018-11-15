def power(number = 1, exp = 1):
    result = 1
    for i in range (1, exp+1):
        result *= number
    return result

def main():
    inputs = str(input("Enter number and exponent separated by space: "))
    inputs = inputs.split(' ')
    number = inputs[0]
    exp = inputs[1]

    if exp.isdigit() and number.isdigit() :
        exp = int(exp)
        number = int(number)
        if exp < 0:
            print("Negative power is not allowed")
        else:
            result = power(number, exp)
            print("{} ^ {} = {}".format(number, exp, result))
    else:
        print("Invalid Inputs")

main()