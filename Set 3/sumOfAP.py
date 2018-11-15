def sumOfAP(a, n, d):
    sum = (n/2)*((2*a) + ((n-1)*d))
    return sum

def main():
    n, a, d = map(int, input("Enter N, A, D separated by space Lower | Upper: ").split(' '))
    result = sumOfAP(a, n, d)
    print(result)
    
main()