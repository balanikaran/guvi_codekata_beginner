def main():
    l, u = map(int, input("Enter range separated by space Lower | Upper: ").split(' '))

    if l > u:
        print("Invalid bounds")
    else:
        for i in range(l+1, u):
            if not i % 2 == 0:
                print(i, end = ' ')

main()