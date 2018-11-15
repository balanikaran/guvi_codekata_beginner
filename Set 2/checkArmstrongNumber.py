def checkArmStrong(number, power):
    sum = 0
    tempNumber = number
    while number > 0:
        temp = number % 10
        sum += temp**power
        number = number // 10
    
    if sum == tempNumber:
        return "YES"
    
    return "NO" 

def main():
    number = input("Enter a number: ")
    if number.isdigit():
        power = len(number)
        number = int(number)
        result = checkArmStrong(number, power)
        print(result)
    else:
        print('Wrong input...')

main()