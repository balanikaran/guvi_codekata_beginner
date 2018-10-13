def sumUptoN(n):
    sum = 0
    for i in range (1, n+1):
        sum += i
    return sum

def main():
    n = int(input("Enter any number: "))
    sum = sumUptoN(n)
    print("{}".format(sum))

main()