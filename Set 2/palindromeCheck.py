def reverse(number):
    reverse = 0
    while number > 0:
        reverse = reverse*10 + number%10
        number //= 10
    
    return reverse

def main():
    number = eval(input("Enter any number to check if it is palindrome or not: "))
    print(type(number))

    if reverse(number) == number:
        print("Yes")
    else:
        print("No")

main()