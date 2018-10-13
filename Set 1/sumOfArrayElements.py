def sumOfArrayElements(arr, k):
    sum = 0
    for i in range(0, k):
        sum += arr[i]
    return sum

def main():
    n = int(input("Enter number of elements in array: "))
    k = int(input("Enter number of elements to be summed: "))
    arr = str(input("Enter array separated with space: "))
    arr = list(map(int, arr.split(' ')))
    
    if len(arr) == n:
        if k > n:
            print("Invalid Input, 'k' cannot be greater than 'n'")
        else:
            print("Sum = {}".format(sumOfArrayElements(arr, k)))
    else:
        print("Invalid Input, length of array doesn't match with specified size")

main()