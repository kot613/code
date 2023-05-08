def is_prime(n):
    prime = "It's a prime number."
    not_prime = "It's not a prime number."
    if n <= 0 or n == 1:
        return not_prime
    i = 2
    while i <= n ** 0.5:
        if n % i == 0:
            return not_prime
        i += 1
    return prime


num = int(input('Enter number: '))
print(is_prime(n=num))