def primes(limit):
    candidates = [True for i in range(limit+1)]
    primes = []
    for value, possible_prime in enumerate(candidates):
        if value < 2:
            continue
        elif possible_prime:
            primes.append(value)
            for i in range(value, len(candidates)):
                if i % value == 0:
                    candidates[i] = False
    return primes
