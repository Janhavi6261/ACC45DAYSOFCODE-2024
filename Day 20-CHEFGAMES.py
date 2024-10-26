def tennis_decision(test_cases):
    results = []
    for case in test_cases:
        
        if all(referee == 0 for referee in case):
            results.append("IN")
        else:
            results.append("OUT")
    return results
T = int(input())
test_cases = []
for _ in range(T):
    test_case = list(map(int, input().split()))
    test_cases.append(test_case)

results = tennis_decision(test_cases)
for result in results:
    print(result)
