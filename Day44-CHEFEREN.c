#include <stdio.h>

int main() {
    int T;
    scanf("%d", &T);  // Number of test cases

    while (T--) {
        int N, A, B;
        scanf("%d %d %d", &N, &A, &B);

        int odd_count = (N + 1) / 2;  // Number of odd-indexed episodes
        int even_count = N / 2;       // Number of even-indexed episodes

        int total_duration = (odd_count * B) + (even_count * A);

        printf("%d\n", total_duration);
    }

    return 0;
}
