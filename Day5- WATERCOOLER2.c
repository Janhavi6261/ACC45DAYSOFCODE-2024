#include <stdio.h>

int main() {
    int T;
    scanf("%d", &T);

    for (int i = 0; i < T; i++) {
        long long X, Y;
        scanf("%lld %lld", &X, &Y);  
        if (X >= Y) {
            printf("0\n");
        } else {
            long long max_months = (Y - 1) / X;
            printf("%lld\n", max_months);
        }
    }

    return 0;
}

