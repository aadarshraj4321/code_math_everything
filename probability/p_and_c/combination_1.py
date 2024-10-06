import math



def combinations(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))



n = 5
r  =3
print(f"C({n}, {r}) = {combinations(n, r)}")
