


def prime_checker(number):
    is_prime = True
    for n in range(2, int(number/2)):
        if number % n == 0:
            is_prime = False
            return is_prime
    return is_prime

print(prime_checker(9))

 