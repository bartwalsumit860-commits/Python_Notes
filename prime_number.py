#program to identify prime number

def prime(n):
    if n < 2:
        print("its not a prime number")
        return
    i = 2
    while i*i<=n:
        if n % i == 0:
            print("its not a prime number")
            return
    print("its prime number")



n = int(input("Enter n: "))

prime(n)


