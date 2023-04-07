# Exercise: genPrimes

# Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls 
# to its next() method: 2, 3, 5, 7, 11, ...

# Have the generator keep a list of the primes it's generated. A candidate number x is prime if (x % p) != 0 for all earlier primes p.

def genPrimes():
    listp,prime = [2,3],2
    yield prime
    prime = 3
    yield prime
    while True:
        a = 0
        try:
            while prime % listp[a] != 0:
                a += 1
            prime += 2
        except IndexError:
            yield prime
            listp.append(prime)

