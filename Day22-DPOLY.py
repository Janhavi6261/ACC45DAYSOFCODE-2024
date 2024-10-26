def find_polynomial_degree(test_cases):
    results = []
    for N, coefficients in test_cases:
        degree = -1
      
        for i in range(N - 1, -1, -1):
            if coefficients[i] != 0:
                degree = i
                break
        results.append(degree)
    return results


T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    coefficients = list(map(int, input().split()))
    test_cases.append((N, coefficients))
results = find_polynomial_degree(test_cases)
for result in results:
    print(result)
