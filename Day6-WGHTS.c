#include <stdio.h>

int canMeasure(int W, int X, int Y, int Z) {
 
    if (W == X || W == Y || W == Z) return 1;
    

    if (W == X + Y || W == X + Z || W == Y + Z) return 1;

 
    if (W == X + Y + Z) return 1;

    return 0;
}

int main() {
    int T;
    scanf("%d", &T);

    while (T--) {
        int W, X, Y, Z;
        scanf("%d %d %d %d", &W, &X, &Y, &Z);
        if (canMeasure(W, X, Y, Z)) {
            printf("YES\n");
        } else {
            printf("NO\n");
        }
    }

    return 0;
}
    

