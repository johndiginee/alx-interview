#!/usr/bin/python3
"""Define a function to generate prime numbers up to a given
maximum using the Sieve of Eratosthenes algorithm."""


def sieve_of_eratosthenes(max_num):
    """Create a list to track prime numbers using
    the Sieve of Eratosthenes algorithm."""
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False
    primes = []

    """Iterate through numbers up to the square root of the maximum number."""
    for num in range(2, int(max_num ** 0.5) + 1):
        if sieve[num]:
            """If the current number is marked as prime,
            add it to the list of primes."""
            primes.append(num)
            """Mark multiples of the current prime as non-prime."""
            for multiple in range(num * num, max_num + 1, num):
                sieve[multiple] = False

    return primes


"""Define the main function for determining the winner of each round."""


def isWinner(x, nums):
    """Calculate the list of primes up to the maximum n."""
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    """Initialize a dictionary to store the results of
    subproblems (memoization)."""
    memo = {}

    """Define a recursive function to check if the current
    player can win with a given n."""
    def canWin(n):
        """Check if the result for n is already memoized."""
        if n in memo:
            return memo[n]

        """Iterate through the list of prime numbers."""
        for prime in primes:
            if prime > n:
                break
            """If the other player cannot win with the
            remaining number (n - prime), the current player wins."""
            if not canWin(n - prime):
                memo[n] = True
                return True

        """If no winning move is found, the current player loses."""
        memo[n] = False
        return False

    """Initialize counters for Maria and Ben's wins."""
    maria_wins = 0
    ben_wins = 0

    """Iterate through the list of n values for each round."""
    for n in nums:
        """Determine the winner for the current round
        using the canWin function."""
        if canWin(n):
            maria_wins += 1
        else:
            ben_wins += 1

    """Compare the number of wins for Maria and Ben and return the result."""
    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
