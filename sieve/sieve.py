def _mark_no_primes(prime, candidates):
    for candidate in range(prime + 1, len(candidates)):
        if candidate % prime == 0:
            candidates[candidate] = False
    return candidates


def primes(limit):
    candidates = [True for i in range(limit+1)]
    primes = []
    for value, possible_prime in enumerate(candidates):
        if (value >= 2 and possible_prime):
            primes.append(value)
            candidates = _mark_no_primes(value, candidates)
    return primes
