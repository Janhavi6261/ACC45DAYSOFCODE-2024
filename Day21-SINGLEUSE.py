def min_attacks_needed(test_cases):
    results = []
    for H, X, Y in test_cases:
       
        normal_attacks = (H + X - 1) // X
        
   
        health_after_special = H - Y
        if health_after_special <= 0:
            total_attacks_with_special = 1
        else:
            special_attacks = (health_after_special + X - 1) // X
            total_attacks_with_special = 1 + special_attacks
        
       
        min_attacks = min(normal_attacks, total_attacks_with_special)
        results.append(min_attacks)
    
    return results


T = int(input())
test_cases = []
for _ in range(T):
    H, X, Y = map(int, input().split())
    test_cases.append((H, X, Y))

results = min_attacks_needed(test_cases)
for result in results:
    print(result)
