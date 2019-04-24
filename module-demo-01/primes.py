

def is_prime(number):
    if number<2:return False

    for test in range(2,number):
        if number%test==0:
            return False

    return True


def prime_range(min,max=None):
    if max is None:
        min,max=2,min

    primes=[]
    for number in range(min,max):
        if is_prime(number):
            primes.append(number)

    return primes

    