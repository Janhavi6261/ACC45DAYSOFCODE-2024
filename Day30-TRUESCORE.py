
T = int(input().strip())


results = []
for _ in range(T):
    
    A, B = map(int, input().strip().split())
    
    C, D = map(int, input().strip().split())
    
  
    if C >= A and D >= B:
        results.append("POSSIBLE")
    else:
        results.append("IMPOSSIBLE")

print("\n".join(results))
