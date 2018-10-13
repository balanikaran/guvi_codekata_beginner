def findLargest(a = 0, b = 0, c = 0):
    if(a > b):
        if(a > c):
            return a
    else:
        if(b > c):
            return b
    return c

def main():
    numbers = input("Enter 3 numbers with space: ")
    listOfNumbers = list(map(int, numbers.split(' ')))
    result = findLargest(listOfNumbers[0], listOfNumbers[1], listOfNumbers[2])
    print("Largest = {}".format(result))

main()