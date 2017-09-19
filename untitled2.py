p = 10000
r = 0.08
t = float(input("how many years? "))
n = 12

A = p * ( (1 + r/n) ** (n*t) )
print(A)
