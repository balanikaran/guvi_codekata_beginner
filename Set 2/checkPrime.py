import math

def main():
    number = int(input("Enter any number to check if it is prime: "))

    isPrime = "Yes"
    for i in range (2, int(math.sqrt(number)) + 1):
        if ((number%i) == 0):
            isPrime = "No"
            break

    print(isPrime)

main()