import math


def permutations(n, r):
    return math.factorial(n) // math.factorial(n - r)


n = 5
r = 3
print(f"P({n}, {r}) = {permutations(n, r)}")
