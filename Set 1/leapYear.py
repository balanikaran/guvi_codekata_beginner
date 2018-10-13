def checkYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return "Leap Year"
            else:
                return "Not a Leap Year"
        else:
            return "Leap Year"
    else:
        return "Not a Leap Year"

def main():
    year = int(input("Enter year: "))
    result = checkYear(year)
    print("{}".format(result))

main()