
#include <stdio.h>

int main() {
    int T; 
    scanf("%d", &T);
    
    while (T--) {
        int N;
        scanf("%d", &N);
        
        int totalPages = N * 1000;
        int notebooks = totalPages / 100;

        printf("%d\n", notebooks);
    }

    return 0;
}