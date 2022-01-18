N = 240
prime_factors = []

def is_prime(num):
    '''
    To make prime list dynamic...
    https://stackoverflow.com/a/568684
    '''
    if num == 0 or num == 1:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    else:
        return True

def primeFactorzation():
    global N, prime_factors
    primes = filter(is_prime, range(0, N))

    while True:
        if is_prime(N):
            prime_factors.append(N)
            break
        for prime in filter(is_prime, range(0, N)):
            if N % prime == 0:
                prime_factors.append(prime)
                N = int(N/prime)
                break


primeFactorzation()
print(prime_factors)
