def isPrime(n):
    """this function checks if the given parameter n is a prime"""
    prime = False;
    for i in range(2,n):
        if ((n%i) == 0):
            prime = True;
    return prime;

def getPrimeNumbers(n):
    """This is the main function that generates a list of the prime numbers between 2 and n"""
    primes = []
    numbers = [x + 1 for x in range(1, n)];

    for num in numbers:
        
        if (isPrime(num) == False):
            primes.append(num);

    return primes


a = getPrimeNumbers(20);
print (a);