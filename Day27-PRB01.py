
import math

def is_prime(n):
   
    if n <= 1:
        return False
  
    if n <= 3:
        return True
  
    if n % 2 == 0 or n % 3 == 0:
        return False
    
  
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True

T = int(input().strip())

results = []
for _ in range(T):
    N = int(input().strip())
   
    results.append("yes" if is_prime(N) else "no")
print("\n".join(results))
