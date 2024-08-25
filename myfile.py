def is_prime(n):
    if n <= 0:
        print(f"{n} is Invalid Input")
    elif n == 1 :
        print(f"{n} is neither prime or composite")
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                print(f"{n} is not a prime number")
                return
        print(f"{n} is not a prime number")



is_prime(number)
