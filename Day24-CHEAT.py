
T = int(input().strip())
results = []
for _ in range(T):
    N = int(input().strip())
    
    if N < 2:
         
        results.append(0)
    else:
      
        count_tuesdays = (N - 2) // 7 + 1
        results.append(count_tuesdays)
        
for result in results:
    print(result)