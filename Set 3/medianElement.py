def main():
    totalElements = input("Enter total elements: ")
    if totalElements.isdigit():
        totalElements = int(totalElements)
        numbers = list(map(int, input("Enter numbers ").split(' ')))
        if len(numbers) == totalElements:
            numbers.sort()
            print(numbers[(totalElements-1)//2])
        else:
            print("More elements then total...")
    else:
        print("Wrong Input...")

main()