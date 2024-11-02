
T = int(input().strip())

results = []
for _ in range(T):
    
    N = int(input().strip())
    
 
    choices = N * (N - 1)
    results.append(choices)

print("\n".join(map(str, results)))
