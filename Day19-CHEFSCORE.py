def can_achieve_exact_marks(N, X, Y):
  
    max_score = N * X
 
    return Y <= max_score and Y % X == 0

def main():
    T = int(input())
    results = []
    for _ in range(T):
        N, X, Y = map(int, input().split())
        if can_achieve_exact_marks(N, X, Y):
            results.append("YES")
        else:
            results.append("NO")
    print("\n".join(results))

if __name__ == "__main__":
    main()

