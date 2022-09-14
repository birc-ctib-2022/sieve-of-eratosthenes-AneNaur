"""Computing primes."""


def sieve(n):#(n: int) -> list[int]:
    """
    Compute all the primes up to (and possibly including) `n`.

    `n` must be positive.

    >>> sieve(15)
    [2, 3, 5, 7, 11, 13]

    """
    assert n > 0
    candidates = list(range(2, n + 1))
    primes = []

    # FIXME: fill out this bit
    while candidates:
        i=1
        len_can=len(candidates)
        while i < len_can:
            p=candidates[0]
            if candidates[i]%p==0:
                candidates.remove(candidates[i])
                len_can-=1
            else:
                i+=1
        primes.append(candidates[0])
        candidates.remove(candidates[0])
    return primes

#print(sieve(15))