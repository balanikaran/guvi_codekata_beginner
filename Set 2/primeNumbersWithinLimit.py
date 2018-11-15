from math import sqrt

def checkPrime(number):
    isPrime = True
    for i in range (2, int(sqrt(number)) + 1):
        if number % i == 0:
            isPrime = False
            break

    return isPrime

def main():
    l, u = map(int, input("Enter range separated by space Lower | Upper: ").split(' '))

    if l > u:
        print("Invalid bounds")
    else:
        for i in range(l+1, u):
            if checkPrime(i):
                print(i, end = ' ')

main()