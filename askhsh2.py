def Fibonacci(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])

    return fib[n]

def pow(a, n, p):
  r = 1
  a = a % p
  while n > 0:
      if n % 2:
          r = (r * a) % p
          n = n - 1
      else:
          a = (a ** 2) % p
          n = n // 2

  return r % p

import random
def isPrime(n, k):
   if n <= 1:
      return False
   if n <= 3:
      return True
   for i in range(k):
      a = random.randint(2, n - 1)
      if pow(a, n - 1, n) != 1:
         return False
   return True

n = int(input("Give n: "))
x = (Fibonacci(n))
print(f"N-th fibonacci number: {x}")
k = 20
if isPrime(x, k):
    print("It's a prime number!")
else:
    print("It's not a number prime...")




