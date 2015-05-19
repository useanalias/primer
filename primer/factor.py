from .utils import eratosthenes, bound

import collections
import math

def trial(n, sieve=True):
    n = bound(n) 
    factors = collections.Counter() 
    upper = int(math.sqrt(n))
    divisors = list(range(2, upper)) if sieve else eratosthenes(upper) 

    for d in divisors:
        while n % d == 0:
            n //= d
            factors[d] += 1

    if n > 1: 
        factors[n] += 1

    return factors


