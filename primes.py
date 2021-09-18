import math
import bisect

def primes_to_n(number):
  if number < 2:
    return []

  primes = [2]
  for candidate in range(3, number, 2):
    root = math.sqrt(candidate)
    root_index = bisect.bisect(primes, root)

    if not any(candidate % prime == 0 for prime in primes[:root_index]):
      primes.append(candidate)

  return primes
