#include <stdio.h>

int main() {
    int T;
    scanf("%d", &T);  // Number of test cases

    while (T--) {
        long long N;
        scanf("%lld", &N);

        long long full_groups = N / 5;
        long long remaining = N % 5;

        long long total_coins = (full_groups * 4) + remaining;

        printf("%lld\n", total_coins);
    }

    return 0;
}
