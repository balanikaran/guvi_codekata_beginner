def checkArmStrong(number):
    sum = 0
    power = len(str(number))
    tempNumber = number
    while number > 0:
        temp = number % 10
        sum += temp**power
        number = number // 10
    
    if sum == tempNumber:
        return True
    
    return False

def main():
    l, u = map(int, input("Enter range separated by space Lower | Upper: ").split(' '))

    if l > u:
        print("Invalid bounds")
    else:
        for i in range(l+1, u):
            if checkArmStrong(i):
                print(i, end = ' ')

main()