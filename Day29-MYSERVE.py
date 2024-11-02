
T = int(input().strip())


results = []
for _ in range(T):
   
    P, Q = map(int, input().strip().split())
    
    
    total_points = P + Q
    
    
    serve_group = total_points // 2
    
    
    if serve_group % 2 == 0:
        results.append("Alice")
    else:
        results.append("Bob")

print("\n".join(results))

