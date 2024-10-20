#include <stdio.h>
#include <math.h>

int main() {
    int T;
    scanf("%d", &T); 

    while (T--) {
        long long N, A, B;
        scanf("%lld %lld %lld", &N, &A, &B);

        
        int rounds = (int)(log2(N));  

        // Calculate total time
        long long totalTime = rounds * A;
        totalTime += (rounds - 1) * B;    

        printf("%lld\n", totalTime); 
    }

    return 0;
}
