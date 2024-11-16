#include <stdio.h>

int main() {
    int T;
    scanf("%d", &T);  // Number of test cases

    while (T--) {
        int N, X, P;
        scanf("%d %d %d", &N, &X, &P);

        int score = 4 * X - N;  // Calculate Chef's score

        if (score >= P) {
            printf("PASS\n");
        } else {
            printf("FAIL\n");
        }
    }

    return 0;
}
