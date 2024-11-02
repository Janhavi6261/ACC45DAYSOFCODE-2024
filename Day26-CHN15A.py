
T = int(input().strip())


for _ in range(T):
    # Read N and K
    N, K = map(int, input().strip().split())
    
    
    characteristics = list(map(int, input().strip().split()))
    
   
    count = 0
    for characteristic in characteristics:
        if (characteristic + K) % 7 == 0:
            count += 1
    
    
    print(count)

