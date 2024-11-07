#include <stdio.h>

int main() {
    int T; 
    scanf("%d", &T);

    while (T--) {
        int A, B;
        scanf("%d %d", &A, &B);

        int required_sum = 21;
        int third_number = required_sum - (A + B);

       
        if (third_number >= 1 && third_number <= 10) {
            printf("%d\n", third_number);
        } else {
            printf("-1\n");
        }
    }

    return 0;
}

