def is_prime(n):
    res = True
    if n <= 1 :
        res = False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                res = False
    return res
